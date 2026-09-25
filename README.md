# Story Homes Land website

A static marketing site for Story Homes Land, the strategic land and promotion division of Story Homes. It follows the layout of a typical land promoter site (hero, key stats, a "why us" section, the promotion process, case studies, testimonials, news, and a landowner enquiry form).

## Pages
- `index.html`: home
- `about.html`: story, values, team
- `landowners.html`: land promotion explained, agreement types, process, site criteria, FAQs
- `projects.html`: case studies with region filter
- `news.html`: news and insights
- `contact.html`: land submission form and offices

## Editing
All pages are generated from `tools/build.py`, which holds the shared header, footer and content (projects, news, team, phone, email). Edit it, then run:

```
python3 tools/build.py
```

Styles are in `assets/css/styles.css` and behaviour (sticky header, mobile menu, count-up stats, testimonial slider, project filters, form handling) is in `assets/js/main.js`.

## Preview
Open `index.html` in a browser, or run `python3 -m http.server` and visit http://localhost:8000.

## Content source
Content is based on the Story Homes Strategic Land page (https://www.storyhomes.co.uk/land-and-planning/strategic-land/) and related Story Homes land and planning news. All copy is paraphrased. Project and news cards link back to the original articles on storyhomes.co.uk.

## Still to replace before launch
- Illustrations in `assets/img/` (swap for real site photography) and the logo (`assets/img/logo.svg`), which should be replaced with the official brand mark
- Team photos (currently silhouettes)
- The enquiry form is front-end only. Connect it to a form service or CRM to receive submissions.
- The Privacy, Cookies and Terms links
- Check that contact details, figures and project stages are current before publishing
