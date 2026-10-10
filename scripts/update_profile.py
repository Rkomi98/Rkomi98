#!/usr/bin/env python3
"""Render profile SVGs from GitHub data; never enumerate private repositories."""

import argparse
from collections import Counter
from datetime import datetime
from html import escape
import json
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
USERNAME = 'Rkomi98'
BG = '#f7f6f3'
INK = '#25313b'
MUTED = '#66727b'
BORDER = '#dfdfd8'
BLUE = '#54748b'
GREEN = '#537c70'
GOLD = '#a88758'


def api(endpoint, query=None):
    args = ['gh', 'api', endpoint]
    if query:
        args.extend(['-f', 'query=' + query])
    result = subprocess.run(args, capture_output=True, text=True, timeout=60)
    if result.returncode:
        raise RuntimeError('GitHub request failed: ' + endpoint)
    payload = json.loads(result.stdout)
    if isinstance(payload, dict) and payload.get('errors'):
        raise RuntimeError('GitHub returned errors: ' + endpoint)
    return payload


def summarise(user, repos, calendar, updated_on):
    public = [r for r in repos if not r.get('private', False)
              and r['owner']['login'].lower() == USERNAME.lower()]
    sources = [r for r in public if not r['fork']]
    languages = Counter(r['language'] for r in sources if r.get('language'))
    # Publish aggregates only: no repository identifiers or private activity detail.
    return {
        'username': USERNAME,
        'updated_on': updated_on,
        'public_repositories': len(public),
        'source_repositories': len(sources),
        'followers': user['followers'],
        'stars_received': sum(r['stargazers_count'] for r in sources),
        'forks_received': sum(r['forks_count'] for r in sources),
        'primary_languages': dict(languages.most_common()),
        'no_detected_language': sum(not r.get('language') for r in sources),
        'calendar': calendar,
    }


def fetch():
    user = api('users/' + USERNAME)
    repos = []
    page = 1
    while True:
        batch = api(f'users/{USERNAME}/repos?per_page=100&type=owner&page={page}')
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    query = ('query { user(login: "' + USERNAME + '") { contributionsCollection { '
             'contributionCalendar { totalContributions weeks { contributionDays { '
             'date contributionCount } } } } } }')
    calendar = api('graphql', query)['data']['user']['contributionsCollection']['contributionCalendar']
    date = datetime.now(ZoneInfo('Europe/Rome')).date().isoformat()
    return summarise(user, repos, calendar, date)


def text(x, y, content, size=14, fill=INK, weight=400, family='Arial, Helvetica, sans-serif', **attrs):
    extra = ' '.join(f'{escape(k.replace("_", "-"))}="{escape(str(v), quote=True)}"' for k, v in attrs.items())
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" {extra}>{escape(str(content))}</text>')


def rect(x, y, width, height, fill, radius=0, stroke=None):
    border = f' stroke="{stroke}"' if stroke else ''
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}"{border}/>'


def line(x1, y1, x2, y2, stroke=BORDER):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}"/>'


def svg(width, height, title, parts):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title, quote=True)}">'
            f'<title>{escape(title)}</title>' + rect(0.5, 0.5, width - 1, height - 1, BG, 12, BORDER)
            + ''.join(parts) + '</svg>\n')


def header():
    p = [text(36, 41, 'MIRKO CALCATERRA / GENAI ENGINEER', 12, MUTED, 600, letter_spacing=2),
         text(34, 113, 'From data to useful tools.', 49, INK, 400, family='Georgia, Times New Roman, serif'),
         text(36, 151, 'AI systems · Geospatial intelligence · Sports technology', 18, MUTED),
         line(36, 176, 754, 176),
         text(36, 206, 'BUILD', 11, GREEN, 600, letter_spacing=2),
         text(136, 206, 'EVALUATE', 11, BLUE, 600, letter_spacing=2),
         text(258, 206, 'EXPLAIN', 11, GOLD, 600, letter_spacing=2)]
    # Orbital and spatial primitives echo EO and modelling, with no external assets.
    for radius in (37, 64, 91):
        p.append(f'<circle cx="903" cy="119" r="{radius}" fill="none" stroke="{BORDER}"/>')
    p.append('<path d="M818 156L868 76L940 67L979 147L904 185Z" fill="none" stroke="#91a69b"/>')
    for x, y, colour in [(818, 156, GREEN), (868, 76, BLUE), (940, 67, GOLD), (979, 147, GREEN), (904, 185, BLUE)]:
        p.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{colour}"/>')
    p.append(f'<circle cx="903" cy="119" r="10" fill="{INK}"/>')
    return svg(1040, 236, 'Mirko Calcaterra — AI engineering, geospatial intelligence, sports technology', p)


def capabilities():
    items = [
        ('ai', '01 / AI SYSTEMS', 'RAG & agent workflows', 'MCP · harnesses · evaluation', GREEN),
        ('geo', '02 / GEOAI', 'Spatial data & applied ML', 'Earth Observation · 3D data', BLUE),
        ('products', '03 / PRODUCTS & PEOPLE', 'Build, teach & analyse', 'Full stack · training · sports', GOLD),
    ]
    cards = {}
    for name, label, title, subtitle, colour in items:
        p = [text(25, 43, label, 10, colour, 600, letter_spacing=1.2),
             text(25, 75, title, 18, INK, 600), text(25, 102, subtitle, 13, MUTED)]
        cards[f'capabilities-{name}.svg'] = svg(340, 141, title + ' — ' + subtitle, p)
    return cards


def statistics(data):
    days = [d for w in data['calendar']['weeks'] for d in w['contributionDays']]
    values = [(data['calendar']['totalContributions'], 'CONTRIBUTIONS', 'Calendar period', GREEN),
              (sum(d['contributionCount'] > 0 for d in days), 'ACTIVE DAYS', 'Days with contributions', BLUE),
              (data['public_repositories'], 'PUBLIC REPOS', f"{data['source_repositories']} non-fork repositories", GOLD),
              (data['followers'], 'FOLLOWERS', 'GitHub profile', GREEN),
              (data['stars_received'], 'STARS RECEIVED', 'Public non-fork repositories', BLUE),
              (data['forks_received'], 'FORKS RECEIVED', 'Public non-fork repositories', GOLD)]
    p = [text(25, 34, 'GitHub, in numbers', 21, INK, 600),
         text(25, 57, 'A snapshot of my work and community', 12, MUTED)]
    for i, (value, label, note, colour) in enumerate(values):
        x = 25 + (i % 3) * 168
        y = 110 + (i // 3) * 97
        p.extend([text(x, y, f'{value:,}', 35, colour, 600),
                  text(x, y + 22, label, 9, INK, 600, letter_spacing=.7),
                  text(x, y + 40, note, 9, MUTED)])
    p.extend([line(25, 264, 495, 264), text(25, 285, 'GitHub API · updated ' + data['updated_on'], 11, MUTED)])
    return svg(520, 306, 'GitHub statistics: contributions, active days, public repositories, followers, stars and forks received', p)


def languages(data):
    top = list(data['primary_languages'].items())[:5]
    other = sum(data['primary_languages'].values()) - sum(n for _, n in top) + data['no_detected_language']
    if other:
        top.append(('Other / no detected language', other))
    max_count = max((n for _, n in top), default=1)
    colours = [GREEN, BLUE, GOLD, '#92728b', '#779499', '#a3aaa3']
    p = [text(25, 34, 'Languages across my projects', 21, INK, 600),
         text(25, 57, 'Repository count by primary language', 12, MUTED)]
    for i, (name, count) in enumerate(top):
        y = 87 + i * 28
        p.extend([text(25, y, name, 12), text(493, y, count, 12, MUTED, text_anchor='end'),
                  rect(25, y + 7, 430, 4, BORDER, 2),
                  rect(25, y + 7, 430 * count / max_count, 4, colours[i], 2)])
    p.extend([line(25, 264, 495, 264), text(25, 285, 'Public non-fork repos · not a skill rating', 11, MUTED)])
    return svg(520, 306, 'Primary language distribution by public non-fork repository count; not proficiency percentages', p)


def activity(data):
    weeks = data['calendar']['weeks']
    days = [d for w in weeks for d in w['contributionDays']]
    max_count = max((d['contributionCount'] for d in days), default=0)
    colours = [BORDER, '#dce8df', '#adc7b8', '#7ba68f', '#476f5b']
    p = [text(25, 35, 'A year of building', 23, INK, 600),
         text(1015, 35, f"{data['calendar']['totalContributions']:,} contributions", 14, GREEN, 600, text_anchor='end')]
    last_month = None
    cell, gap = 13, 4
    for wi, week in enumerate(weeks):
        x = 57 + wi * (cell + gap)
        for day in week['contributionDays']:
            date = datetime.strptime(day['date'], '%Y-%m-%d')
            dow = (date.weekday() + 1) % 7
            if date.month != last_month:
                if wi < len(weeks) - 1:
                    p.append(text(x, 62, date.strftime('%b'), 10, MUTED))
                last_month = date.month
            count = day['contributionCount']
            level = 0 if not count else min(4, 1 + int(count / max(1, max_count) * 3))
            p.append(f'<g><title>{escape(day["date"])}: {count} contributions</title>'
                     + rect(x, 74 + dow * (cell + gap), cell, cell, colours[level], 2) + '</g>')
    for y, label in [(104, 'Mon'), (138, 'Wed'), (172, 'Fri')]:
        p.append(text(25, y, label, 9, MUTED))
    period = days[0]['date'] + ' — ' + days[-1]['date'] if days else 'No contribution data'
    p.extend([text(25, 223, period + ' · GitHub contribution calendar', 11, MUTED),
              text(850, 223, 'Less', 10, MUTED), text(990, 223, 'More', 10, MUTED)])
    for i, colour in enumerate(colours):
        p.append(rect(880 + i * 19, 212, 13, 13, colour, 2))
    return svg(1040, 246, 'GitHub contribution heatmap over the calendar period', p)


def render(data):
    ASSETS.mkdir(exist_ok=True)
    images = {'header.svg': header(), **capabilities(),
              'github-stats.svg': statistics(data), 'languages.svg': languages(data),
              'activity.svg': activity(data)}
    for name, content in images.items():
        (ASSETS / name).write_text(content, encoding='utf-8')
    return len(images)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render-only', action='store_true', help='Render the saved snapshot without network access.')
    args = parser.parse_args()
    path = ASSETS / 'profile-data.json'
    data = json.loads(path.read_text()) if args.render_only else fetch()
    count = render(data)
    if not args.render_only:
        path.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(f'Rendered {count} SVG assets from GitHub aggregate data.')


if __name__ == '__main__':
    main()
