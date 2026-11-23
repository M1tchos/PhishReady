# PhishReady — Python edition

Python version of the supplied dissertation prototype: **Assessing the Influence of Cybersecurity Awareness on Phishing Readiness Among University Students**.

## Run locally

Install Python 3.10 or later, open a terminal in this folder, and run:

```sh
python app.py
```

On Windows you can also use `py app.py`; on macOS/Linux use `python3 app.py` if needed. Open http://127.0.0.1:8000 in your browser. Stop with Ctrl+C. No pip dependencies or internet connection are needed after Python is installed. To use another port: `python app.py --port 8080`.

## Fidelity to the original

The original index.html and styles.css are copied byte for byte. All 20 scenarios, wording, visual design, responsive layout, charts, guide, certificate, reports, demo analytics and local history are preserved. Python now selects five distinct random scenarios, checks classifications, computes scores and supplies the original personalised recommendations. JavaScript remains for browser rendering, localStorage, canvas charts, printing and downloads. This is a Python-backed web app, not a desktop GUI or a pure-Python browser interface.

Profiles and history stay in browser localStorage, using the original keys. Only scenario IDs and selected classifications are sent to the Python service; it does not save those requests or receive names/student numbers. Browser data belongs to the website origin: history from a double-clicked HTML file will not automatically appear at localhost. Keep the same host and port to reuse history. Run the Python server to use this edition; opening static/index.html directly does not connect its APIs.

The original recommendation fallback is deliberately retained, even for mistakes outside its three targeted category groups. The cohort analytics remain simulated, not actual research findings.

## Repository contents

- `app.py`: local HTTP server and JSON endpoints
- `core.py`: Python assessment and recommendation rules
- `scenarios.json`: the original 20 scenarios, unchanged
- `static/`: original HTML/CSS and adapted browser interactions
- `tests/`: scoring, API and validation checks

Run checks with `python -m unittest discover -s tests -v`.

## GitHub

Upload the contents of **this folder** as the repository root, including static/ and scenarios.json. There are no secrets or third-party packages to configure. GitHub stores this code; GitHub Pages cannot run the Python server. The bundled standard-library server is intended for local prototype use. Public deployment needs a suitable Python hosting setup.

## Research ethics

This is a safe simulation. It sends no phishing messages, follows no scenario links, and collects no passwords, OTPs or banking credentials. Demo cohort statistics must not be presented as dissertation research results. Certificates are prototype output, not official institutional certificates.
