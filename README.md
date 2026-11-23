# PhishReady — Python edition

Python version of the supplied dissertation prototype: **Assessing the Influence of Cybersecurity Awareness on Phishing Readiness Among University Students**.

## Run locally

Install Python 3.10 or later, open a terminal in this folder, and run:

```sh
python app.py
```

On Windows you can also use `py app.py`; on macOS/Linux use `python3 app.py` if needed. Open http://127.0.0.1:8000 in your browser. Stop with Ctrl+C. No pip dependencies or internet connection are needed after Python is installed. To use another port: `python app.py --port 8080`.

## Repository contents

- `app.py`: local HTTP server and JSON endpoints
- `core.py`: Python assessment and recommendation rules
- `scenarios.json`: the original 20 scenarios, unchanged
- `static/`: original HTML/CSS and adapted browser interactions
- `tests/`: scoring, API and validation checks

Run checks with `python -m unittest discover -s tests -v`.



## Research ethics

This is a safe simulation. It sends no phishing messages, follows no scenario links, and collects no passwords, OTPs or banking credentials. Demo cohort statistics must not be presented as dissertation research results. Certificates are prototype output, not official institutional certificates.
