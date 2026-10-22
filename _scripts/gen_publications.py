#!/usr/bin/env python3
"""从 publications.bib 生成 Jekyll 静态论文列表 (_pages/publications.md)。

用法:
    python3 gen_publications.py <input.bib> <output.md>
BibBase 在部分网络不可用，改用静态列表，无外部依赖。
"""
import re
import sys
import unicodedata

ENTRY_RE = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', re.S)


def split_entries(text):
    """Yield (type, key, body) for each bib entry."""
    for m in ENTRY_RE.finditer(text):
        start = m.end()
        depth = 1
        i = start
        while i < len(text) and depth > 0:
            ch = text[i]
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            i += 1
        yield m.group(1).lower(), m.group(2), text[start:i - 1]


def parse_fields(body):
    fields = {}
    i = 0
    n = len(body)
    while i < n:
        while i < n and body[i] in ' \t\r\n,':
            i += 1
        m = re.match(r'([A-Za-z_\-]+)\s*=\s*', body[i:])
        if not m:
            break
        name = m.group(1).lower()
        i += m.end()
        if i < n and body[i] == '{':
            depth = 1
            value_start = i + 1
            i += 1
            while i < n and depth > 0:
                if body[i] == '{':
                    depth += 1
                elif body[i] == '}':
                    depth -= 1
                i += 1
            value = body[value_start:i - 1]
        elif i < n and body[i] == '"':
            value_start = i + 1
            i += 1
            while i < n and body[i] != '"':
                i += 1
            value = body[value_start:i]
            i += 1
        else:
            m2 = re.match(r'[^,\n]+', body[i:])
            value = m2.group(0) if m2 else ''
            i += len(value)
        fields[name] = value.strip()
    return fields


def clean(text):
    t = text
    t = t.replace(r'\{', '').replace(r'\}', '')
    t = re.sub(r'\\[a-zA-Z]+\s*', '', t)
    t = re.sub(r'\\([&%#_$^])', r'\1', t)
    t = t.replace('$', '')
    t = re.sub(r'[{}]', '', t)
    t = t.replace('~', ' ')
    t = t.replace('--', '–')
    t = re.sub(r'\s+', ' ', t).strip()
    t = t.replace('_', r'\_').replace('*', r'\*')
    return t


# bib 里信息卡写得不好看的个别条目，直接人工定稿
TITLE_OVERRIDES = {
    'he2023s': 'S²Loop: A Lightweight Spectral-Spatio Loop Closure Detector for Resource-Constrained Platforms',
}


def fmt_authors(raw):
    people = [p.strip() for p in re.split(r'\s+and\s+', raw) if p.strip()]
    out = []
    for p in people:
        if ',' in p:
            last, first = p.split(',', 1)
            name = f'{first.strip()} {last.strip()}'
        else:
            name = p
        name = clean(name)
        if name.endswith('Cheng Liu') or name == 'Cheng Liu':
            name = f'**{name}**'
        out.append(name)
    return ', '.join(out)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    text = open(src, encoding='utf-8').read()
    items = []
    for typ, key, body in split_entries(text):
        f = parse_fields(body)
        year = f.get('year', '').strip()
        title = TITLE_OVERRIDES.get(key) or clean(f.get('title', '(no title)'))
        venue = clean(f.get('booktitle') or f.get('journal') or '')
        authors = fmt_authors(f.get('author', ''))
        ranking = clean(f.get('ranking', ''))
        link = f.get('url') or (f'https://doi.org/{f["doi"]}' if f.get('doi') else '')
        items.append(dict(year=year, title=title, venue=venue, authors=authors,
                          ranking=ranking, link=link, typ=typ, key=key))

    items.sort(key=lambda x: (x['year'], x['key']), reverse=True)
    lines = ['---', 'layout: archive', 'title: "Publications"',
             'permalink: /publications/', 'author_profile: true', 'classes: wide',
             '---', '', '{% include base_path %}', '']
    cur = None
    for it in items:
        if it['year'] != cur:
            cur = it['year']
            lines.append(f'## {cur}')
            lines.append('')
        seg = f"- **{it['title']}**"
        if it['authors']:
            seg += f"<br>{it['authors']}"
        tail = []
        if it['venue']:
            tail.append(f"*{it['venue']}*")
        tail.append(it['year'])
        if it['ranking']:
            tail.append(f"[{it['ranking']}]")
        seg += '<br>' + ', '.join(tail)
        if it['link']:
            seg += f" · [link]({it['link']})"
        lines.append(seg)
    open(dst, 'w', encoding='utf-8').write('\n'.join(lines))
    print(f'{len(items)} entries -> {dst}')


if __name__ == '__main__':
    main()
