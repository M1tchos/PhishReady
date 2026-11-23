"""Original PhishReady assessment rules, implemented in Python."""
import json
import random
from pathlib import Path

SCENARIOS = json.loads(Path(__file__).with_name('scenarios.json').read_text(encoding='utf-8'))
BY_ID = {s['id']: s for s in SCENARIOS}
CHOICES = ('Legitimate', 'Suspicious', 'Phishing')


def new_assessment():
    return random.sample(SCENARIOS, 5)


def classify(scenario_id, choice):
    if type(scenario_id) is not int or scenario_id not in BY_ID or choice not in CHOICES:
        raise ValueError('Invalid scenario or classification')
    scenario = BY_ID[scenario_id]
    return dict(id=scenario_id, category=scenario['category'], answer=choice,
                correctAnswer=scenario['answer'], correct=choice == scenario['answer'])


def readiness_band(score):
    if score >= 80:
        return 'High Readiness'
    if score >= 60:
        return 'Developing Readiness'
    return 'Needs Support'


def recommendations(answers):
    mistakes = {a['category'] for a in answers if not a['correct']}
    recs = []
    if mistakes.intersection(('Account Security', 'MFA / Verification', 'Password Hygiene', 'Account Recovery')):
        recs.append('Never share passwords or OTPs, and independently verify unexpected account-security messages.')
    if mistakes.intersection(('Reward Scam', 'Job Scam', 'Bursary Offer', 'Parcel Delivery')):
        recs.append('Treat unexpected rewards, jobs, deliveries and bursary offers carefully when they request sensitive information or payment.')
    if mistakes.intersection(('Collaboration Platform', 'Cloud Storage', 'Meeting Invite', 'QR Phishing')):
        recs.append('Verify meeting invitations, shared files and QR-based requests through official channels before signing in.')
    if not recs:
        recs.append('Your classifications were strong. Continue practising with new random scenario combinations to reinforce readiness.')
    recs.append('Pause when a message creates urgency, inspect the sender/domain, and report suspicious messages through trusted institutional channels.')
    return recs


def evaluate(submissions):
    if not isinstance(submissions, list) or len(submissions) != 5:
        raise ValueError('Exactly five answers are required')
    if any(not isinstance(a, dict) for a in submissions):
        raise ValueError('Invalid answer')
    answers = [classify(a.get('id'), a.get('choice')) for a in submissions]
    if len({a['id'] for a in answers}) != 5:
        raise ValueError('Scenarios must be distinct')
    correct = sum(a['correct'] for a in answers)
    score = correct * 20
    return dict(correct=correct, score=score, total=5, answers=answers,
                band=readiness_band(score), recommendations=recommendations(answers))
