"""Run with python app.py. No third-party dependencies required."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from core import SCENARIOS, classify, evaluate, new_assessment

STATIC = Path(__file__).resolve().parent / 'static'
ASSETS = {'/': ('index.html', 'text/html'), '/index.html': ('index.html', 'text/html'),
          '/styles.css': ('styles.css', 'text/css'), '/app.js': ('app.js', 'text/javascript')}


class Handler(BaseHTTPRequestHandler):
    def respond(self, body, content_type, status=200):
        self.send_response(status)
        self.send_header('Content-Type', content_type + '; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write(body)

    def json_response(self, data, status=200):
        self.respond(json.dumps(data, ensure_ascii=False).encode('utf-8'), 'application/json', status)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path in ASSETS:
            filename, mime = ASSETS[path]
            self.respond((STATIC / filename).read_bytes(), mime)
        elif path == '/api/scenarios':
            self.json_response(SCENARIOS)
        elif path == '/api/assessment':
            self.json_response(new_assessment())
        else:
            self.json_response({'error': 'Not found'}, 404)

    def do_POST(self):
        path = urlsplit(self.path).path
        if path not in ('/api/answer', '/api/result'):
            self.json_response({'error': 'Not found'}, 404)
            return
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 16384:
                raise ValueError('Invalid request size')
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict):
                raise ValueError('Expected a JSON object')
            result = (classify(data.get('id'), data.get('choice')) if path == '/api/answer'
                      else evaluate(data.get('answers')))
        except (ValueError, TypeError, UnicodeError) as error:
            self.json_response({'error': str(error)}, 400)
            return
        self.json_response(result)


def main():
    parser = argparse.ArgumentParser(description='PhishReady Python prototype')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    with ThreadingHTTPServer((args.host, args.port), Handler) as server:
        print(f'PhishReady running at http://{args.host}:{args.port} (Ctrl+C to stop)', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
