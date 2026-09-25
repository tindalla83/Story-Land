import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE = "01257 443 250"
EMAIL = "John.Winstanley@storyhomes.co.uk"
SH = "https://www.storyhomes.co.uk"
CONTACTS = [
 ("John Winstanley", "Managing Director, Strategic Land", "01257 443 250", "John.Winstanley@storyhomes.co.uk"),
 ("David Robinson", "Head of Strategic Land, North East &amp; North Cumbria", "0191 917 8605", "David.Robinson@storyhomes.co.uk"),
]

NAV = [("index.html","Home"),("about.html","About Us"),("landowners.html","For Landowners"),("projects.html","Projects"),("news.html","News")]

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
"""

CUR = ' aria-current="page"'
def header(active, solid=False):
    links = "\n".join(
        f'        <li><a href="{h}"{CUR if h==active else ""}>{t}</a></li>' for h,t in NAV)
    cls = "site-header site-header--solid" if solid else "site-header"
    return f"""<header class="{cls}">
  <div class="container">
    <nav class="nav" aria-label="Main">
      <a class="logo" href="index.html" aria-label="Story Homes Land home">
        <img class="logo__mark" src="assets/img/logo.svg" alt="">
        <span class="logo__text">Story Homes<small>Land</small></span>
      </a>
      <button class="nav__toggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
      <ul class="nav__links">
{links}
        <li><a class="btn btn--primary" href="contact.html">Contact Us</a></li>
      </ul>
    </nav>
  </div>
</header>
"""

FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo" href="index.html"><img class="logo__mark" src="assets/img/logo.svg" alt=""><span class="logo__text">Story Homes<small>Land</small></span></a>
        <p style="margin-top:20px">The dedicated Strategic Land division of Story Homes. We promote and buy land across the North West, North East, Cumbria and Scotland.</p>
        <div class="socials">
          <a href="#" aria-label="LinkedIn"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.5c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21H9z"/></svg></a>
          <a href="#" aria-label="X"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18.2 2H21l-6.6 7.5L22 22h-6l-4.7-6.2L5.8 22H3l7-8L2 2h6.1l4.3 5.7zM17.2 20h1.6L7 3.8H5.3z"/></svg></a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="landowners.html">For Landowners</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="news.html">News</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="landowners.html#promotion">Strategic Land Promotion</a></li>
          <li><a href="landowners.html#options">Deal Structures</a></li>
          <li><a href="landowners.html#sales">Land with Planning</a></li>
          <li><a href="{SH}/land-and-planning/planning-applications/" target="_blank" rel="noopener">Planning Applications</a></li>
          <li><a href="{SH}/" target="_blank" rel="noopener">Story Homes</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li>John Winstanley<br><a href="tel:01257443250">01257 443 250</a></li>
          <li>David Robinson<br><a href="tel:01919178605">0191 917 8605</a></li>
          <li><a href="contact.html">All contact details</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> Story Homes Land. All rights reserved.</span>
      <span><a href="#">Privacy Policy</a> &nbsp;·&nbsp; <a href="#">Cookies</a> &nbsp;·&nbsp; <a href="#">Terms</a></span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

def page_hero(crumb, title, sub, img="hero-landscape.svg"):
    return f"""<section class="page-hero">
  <div class="page-hero__bg"><img src="assets/img/{img}" alt=""></div>
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / {crumb}</div>
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</section>
"""

CTA = f"""<section class="section">
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>Do you own land with development potential?</h2>
        <p>We welcome approaches from landowners and agents. Get in touch and a member of our Strategic Land team will respond quickly with a clear decision on your site.</p>
      </div>
      <div class="cta-band__actions">
        <a class="btn btn--primary arrow" href="contact.html">Submit your land</a>
        <a class="cta-band__phone" href="tel:{PHONE.replace(' ','')}">or call {PHONE}</a>
      </div>
    </div>
  </div>
</section>
"""

ICON = {
 "shield": '<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
 "pound": '<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17 20H7c2-2 2-4 2-7V8a4 4 0 0 1 7.5-2M6 13h8"/></svg>',
 "map": '<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2zM9 4v14M15 6v14"/></svg>',
 "people": '<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.5 3.4-5.5 6.5-5.5s5.7 2 6.5 5.5"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c2.3 0 4 1.5 4.5 4"/></svg>',
 "home": '<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 11l9-7 9 7v9H3z"/><path d="M10 20v-5h4v5"/></svg>',
 "leaf": '<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 19C5 9 11 4 20 4c0 9-5 15-15 15zM5 19l8-8"/></svg>',
}

PROJECTS = [
 ("north-west","Lancashire","Former Camelot Theme Park","village.svg","Outline planning permission for new homes on a former leisure site, including affordable housing and community benefits.","350","Outline consent","/stories/story-homes-welcomes-outline-planning-permission-for-350-new-homes-on-former-camelot-theme-park-site/"),
 ("north-west","Preston","Lea Road","masterplan.svg","Detailed permission for 161 homes on the northern parcel and outline permission for up to 120 on the southern parcel.","281","Consented","/stories/story-homes-receives-green-light-to-bring-up-to-281-new-high-quality-homes-to-preston/"),
 ("north-west","Lancashire","Cuerdale Garden Village","hero-landscape.svg","An outline application for a new garden village with homes, employment space, a local centre and a primary school.","1,300","Application submitted",""),
 ("north-east","Newcastle upon Tyne","Killingworth Moor","fields.svg","Around 34 hectares bought from Northumberland Estates. It follows earlier deals together at Rake Lane and Alnwick.","34 ha","Land acquired","/stories/story-homes-purchases-landmark-new-site-at-killingworth-moor-newcastle-upon-tyne/"),
 ("north-west","Fylde","Wrea Green","village.svg","Outline planning permission secured for new homes on the edge of the village.","100","Outline consent","/outline-planning-permission-granted-for-wrea-green-homes/"),
 ("cumbria","Cumbria","Land east of The Thorpe, Greystoke","fields.svg","Outline planning permission for a sensitively scaled scheme of new homes in the village.","40","Outline consent","/outline-planning-permission-granted-for-homes-in-greystoke/"),
 ("north-west","Chorley","Coppull","meeting.svg","Planning approval for a new neighbourhood of high-quality family homes.","118","Consented","/stories/story-homes-receives-green-light-to-bring-118-high-quality-new-homes-to-coppull/"),
 ("cumbria","Cumbria","Clifton, Penrith","village.svg","Plans for new homes in Clifton approved by the local planning authority.","","Approved","/eden-district-council-approves-plans-for-homes-in-clifton-penrith/"),
 ("north-west","Lancashire","Halton","masterplan.svg","Outline planning permission granted for new homes.","","Outline consent","/outline-planning-permission-granted-for-homes-in-halton/"),
]

def project_card(p, delay=""):
    region, rname, name, img, text, homes, status, link = p
    href = SH + link if link else "projects.html"
    ext = ' target="_blank" rel="noopener"' if link else ""
    unit = "site area" if "ha" in homes else "homes"
    facts = f'<div class="card__facts"><span><strong>{homes}</strong>{unit}</span><span><strong>{status}</strong>stage</span></div>' if homes else f'<div class="card__facts"><span><strong>{status}</strong>stage</span></div>'
    return f"""      <article class="card reveal" data-region="{region}">
        <div class="card__media"><img src="assets/img/{img}" alt="Illustration of {name}"></div>
        <div class="card__body">
          <div class="card__meta">{rname}</div>
          <h3>{name}</h3>
          <p>{text}</p>
          {facts}
          <a class="card__link" href="{href}"{ext}>{"Read the story" if link else "Find out more"}</a>
        </div>
      </article>"""

NEWS = [
 ("meeting.svg","Company","Story Homes appoints new Head of Land North West","A new appointment to lead land acquisition across the North West.","/story-homes-appoints-new-head-of-land-north-west-to-drive-acquisition-strategy/"),
 ("fields.svg","Land","Landmark site purchased at Killingworth Moor","Around 34 hectares bought from Northumberland Estates, continuing a long-standing relationship.","/stories/story-homes-purchases-landmark-new-site-at-killingworth-moor-newcastle-upon-tyne/"),
 ("village.svg","Planning","Outline consent for 350 homes at the former Camelot site","Permission to regenerate a former theme park with new homes and community benefits.","/stories/story-homes-welcomes-outline-planning-permission-for-350-new-homes-on-former-camelot-theme-park-site/"),
 ("masterplan.svg","Planning","Green light for up to 281 homes in Preston","Detailed and outline permissions secured across two parcels at Lea Road.","/stories/story-homes-receives-green-light-to-bring-up-to-281-new-high-quality-homes-to-preston/"),
 ("meeting.svg","Company","Investment in the North East Land and Planning team","Strengthening the team ahead of planned growth in the North East.","/investment-in-land-and-planning-team-ahead-of-planned-growth-in-the-north-east/"),
 ("hero-landscape.svg","Company","Story Homes and Story Contracting celebrate 35 years","Marking 35 years of building homes and communities.","/story-homes-and-story-contracting-celebrate-35th-anniversary/"),
]

def news_card(n):
    img, cat, title, text, link = n
    return f"""      <article class="card reveal">
        <div class="card__media"><img src="assets/img/{img}" alt=""></div>
        <div class="card__body">
          <div class="card__meta">{cat}</div>
          <h3>{title}</h3>
          <p>{text}</p>
          <a class="card__link" href="{SH}{link}" target="_blank" rel="noopener">Read on storyhomes.co.uk</a>
        </div>
      </article>"""

TESTIMONIALS = f"""<section class="section section--cream">
  <div class="container split">
    <div class="split__media reveal"><img src="assets/img/fields.svg" alt=""></div>
    <div class="reveal">
      <span class="eyebrow">Partnership in practice</span>
      <h2>Long-term relationships with landowners</h2>
      <p>Our work with Northumberland Estates shows how we partner. After successful deals together at Rake Lane and Alnwick, we bought around 34 hectares at Killingworth Moor in Newcastle upon Tyne.</p>
      <p>Many landowners come back to us, or recommend us, because we make quick decisions, deal in good faith and do what we say.</p>
      <a class="btn btn--outline arrow" href="{SH}/stories/story-homes-purchases-landmark-new-site-at-killingworth-moor-newcastle-upon-tyne/" target="_blank" rel="noopener">Read about Killingworth Moor</a>
    </div>
  </div>
</section>
"""

def write(name, html):
    with open(os.path.join(ROOT, name), "w") as f: f.write(html)

# ---------------- HOME ----------------
home = head("Story Homes Land | Strategic Land & Promotion", "Story Homes Land works in partnership with landowners to promote land through the planning system and maximise its value.") + header("index.html") + f"""<main>
<section class="hero">
  <div class="hero__bg"><img src="assets/img/hero-landscape.svg" alt=""></div>
  <div class="container">
    <div class="hero__content">
      <span class="eyebrow" style="color:var(--gold)">Strategic Land &amp; Promotion</span>
      <h1>Unlocking the true value of your land</h1>
      <p>The dedicated Strategic Land division of Story Homes. Our approach is simple and commercial, and it aims to get the most value from your land at the point planning permission is granted.</p>
      <div class="hero__ctas">
        <a class="btn btn--primary arrow" href="contact.html">Submit your land</a>
        <a class="btn btn--ghost" href="landowners.html">How it works</a>
      </div>
    </div>
  </div>
  <a class="hero__scroll" href="#intro">Scroll</a>
</section>

<div class="stats" aria-label="Key figures">
  <div class="stat"><div class="stat__num" data-count="35" data-suffix="+">35+</div><div class="stat__label">Years of Story Homes</div></div>
  <div class="stat"><div class="stat__num" data-count="4">4</div><div class="stat__label">Regions: North West, North East, Cumbria &amp; Scotland</div></div>
  <div class="stat"><div class="stat__num" data-count="100" data-suffix="%">100%</div><div class="stat__label">Promotion costs funded by us</div></div>
  <div class="stat"><div class="stat__num" data-count="15">15</div><div class="stat__label">Years: how far ahead our strategic pipeline looks</div></div>
</div>

<section class="section" id="intro">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2>A land promoter with a housebuilder behind it</h2>
      <p class="lead">Story Homes has a dedicated Strategic Land division. It handles land that is ready to develop now as well as longer-term strategic sites.</p>
      <p>We're always looking for new sites and opportunities, and we welcome approaches from landowners and agents. Our management structure lets us shape each deal around what the individual landowner needs.</p>
      <ul class="checklist">
        <li>We finance every part of the land promotion, keeping your risk low</li>
        <li>Quick decisions on whether we want to buy your site</li>
        <li>We work in good faith from first conversation to completion</li>
      </ul>
      <a class="btn btn--outline arrow" href="about.html">About Story Homes Land</a>
    </div>
    <div class="split__media reveal"><img src="assets/img/meeting.svg" alt="Illustration of a landowner meeting with the land team"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="center reveal">
      <span class="eyebrow">Why work with us</span>
      <h2>A partnership built on trust</h2>
      <p class="lead">No two landowners are the same. We shape each deal around your needs and keep the process simple and commercial.</p>
    </div>
    <div class="grid grid--3" style="margin-top:48px">
      <div class="feature reveal"><div class="feature__icon">{ICON['shield']}</div><h3>We fund promotion</h3><p>We finance every part of promoting your land through planning, keeping your risk low.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['pound']}</div><h3>Maximising value</h3><p>Our approach is designed to get the most value from your land when planning permission is secured.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['map']}</div><h3>Regional teams</h3><p>Land and planning specialists across the North West, North East, Cumbria and Scotland.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['people']}</div><h3>Speedy decisions</h3><p>You'll get a quick answer on whether your site is one we'd look to buy, with no drawn-out uncertainty.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['home']}</div><h3>Flexible deal structures</h3><p>Our management structure lets us tailor terms to each landowner's requirements.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['leaf']}</div><h3>Good faith</h3><p>Straightforward, honest dealings throughout, backed by a housebuilder that builds the homes itself.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="center reveal">
      <span class="eyebrow">Our process</span>
      <h2>From field to planning permission</h2>
      <p class="lead">Some sites already have outline planning permission. Others are short, medium or long-term strategic sites that could take up to 15 years to come forward. We handle both.</p>
    </div>
    <div class="process">
      <div class="step reveal"><div class="step__num"></div><h3>Appraisal</h3><p>A free, confidential assessment of your land's potential.</p></div>
      <div class="step reveal"><div class="step__num"></div><h3>Agreement</h3><p>A tailored promotion or option agreement that works for you.</p></div>
      <div class="step reveal"><div class="step__num"></div><h3>Promotion</h3><p>Engaging with the Local Plan and building the case for development.</p></div>
      <div class="step reveal"><div class="step__num"></div><h3>Planning</h3><p>Preparing and submitting a high-quality planning application.</p></div>
      <div class="step reveal"><div class="step__num"></div><h3>Sale</h3><p>Securing the best value for your land once consent is granted.</p></div>
    </div>
    <div class="center" style="margin-top:48px"><a class="btn btn--primary arrow" href="landowners.html">Learn more about the process</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:20px;margin-bottom:40px">
      <div class="reveal"><span class="eyebrow">Our projects</span><h2 style="margin:0">Recent planning successes</h2></div>
      <a class="btn btn--outline arrow" href="projects.html">View all projects</a>
    </div>
    <div class="grid grid--3">
{chr(10).join(project_card(p) for p in PROJECTS[:3])}
    </div>
  </div>
</section>

{TESTIMONIALS}

<section class="section">
  <div class="container">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:20px;margin-bottom:40px">
      <div class="reveal"><span class="eyebrow">Latest news</span><h2 style="margin:0">News &amp; insights</h2></div>
      <a class="btn btn--outline arrow" href="news.html">All news</a>
    </div>
    <div class="grid grid--3">
{chr(10).join(news_card(n) for n in NEWS[:3])}
    </div>
  </div>
</section>

{CTA}
</main>
""" + FOOTER
write("index.html", home)

# ---------------- ABOUT ----------------
TEAM = [(n, r) for n, r, _, _ in CONTACTS]
team_html = "\n".join(f"""      <div class="person reveal"><div class="person__photo"><svg viewBox="0 0 200 200"><rect width="200" height="200" fill="#e6f0eb"/><circle cx="100" cy="80" r="36" fill="#9dbd98"/><path d="M30 200c6-44 36-66 70-66s64 22 70 66z" fill="#3d8a6c"/></svg></div><h3>{n}</h3><p>{r}</p></div>""" for n,r in TEAM)

about = head("About Us | Story Homes Land", "Story Homes Land is the strategic land division of Story Homes.") + header("about.html") + page_hero("About Us","About Story Homes Land","The strategic land specialists within Story Homes, combining land promotion expertise with the delivery strength of an established housebuilder.") + f"""<main>
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Our story</span>
      <h2>Rooted in the North, built on relationships</h2>
      <p>Story Homes builds new homes across the North East, North West, Cumbria and Scotland. Together with Story Contracting, it recently celebrated 35 years in business.</p>
      <p>Our Strategic Land division sources the land those homes are built on. We look for a region-by-region mix: sites that already have outline planning permission, and short, medium and long-term strategic sites without planning today, some taking up to 15 years to come forward.</p>
      <p>Because we build the homes ourselves, we know what makes a site deliverable. We can take land from promotion through planning to a finished new community.</p>
    </div>
    <div class="split__media reveal"><img src="assets/img/village.svg" alt="Illustration of new homes"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">Our values</span><h2>What guides us</h2></div>
    <div class="grid grid--4" style="margin-top:48px">
      <div class="feature reveal"><h3>Good faith</h3><p>We are honest about a site's prospects and act in good faith throughout.</p></div>
      <div class="feature reveal"><h3>Partnership</h3><p>We treat landowners as long-term partners, not transactions.</p></div>
      <div class="feature reveal"><h3>Speed</h3><p>We give quick decisions so landowners aren't left waiting.</p></div>
      <div class="feature reveal"><h3>Commercial focus</h3><p>A simple, commercial approach to getting the most value from your land.</p></div>
    </div>
  </div>
</section>

<div class="stats" aria-label="Key figures">
  <div class="stat"><div class="stat__num" data-count="35" data-suffix="+">35+</div><div class="stat__label">Years of Story Homes</div></div>
  <div class="stat"><div class="stat__num" data-count="4">4</div><div class="stat__label">Regions: North West, North East, Cumbria &amp; Scotland</div></div>
  <div class="stat"><div class="stat__num" data-count="100" data-suffix="%">100%</div><div class="stat__label">Promotion costs funded by us</div></div>
  <div class="stat"><div class="stat__num" data-count="15">15</div><div class="stat__label">Years: how far ahead our strategic pipeline looks</div></div>
</div>

<section class="section" id="team">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">Our people</span><h2>Meet the team</h2><p class="lead">Talk to the people who lead our Strategic Land business.</p></div>
    <div class="grid grid--2" style="margin-top:48px;max-width:760px;margin-left:auto;margin-right:auto">
{team_html}
    </div>
  </div>
</section>

{CTA}
</main>
""" + FOOTER
write("about.html", about)

# ---------------- LANDOWNERS ----------------
land = head("For Landowners | Story Homes Land", "How Story Homes Land works with landowners to promote land and maximise its value.") + header("landowners.html") + page_hero("For Landowners","Working with landowners","Whether your land already has planning or is a long-term prospect, we'll shape a deal around you and give you a quick, clear decision.", "fields.svg") + f"""<main>
<section class="section" id="promotion">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Land promotion</span>
      <h2>What is land promotion?</h2>
      <p>Land promotion is the process of securing planning permission on land that is currently undeveloped, so it can be sold for development at a much higher value than its existing use.</p>
      <p>Obtaining planning permission is complex, expensive and uncertain. A land promoter takes on that cost and risk, bringing the expertise needed to navigate Local Plans, technical studies and planning applications.</p>
      <p>Story Homes will finance all aspects of the land promotion and keep your risk low. We aim to get the most value from your land at the point planning permission is secured.</p>
      <ul class="checklist">
        <li>We fund the promotion, so you don't carry the cost</li>
        <li>Deals shaped around your requirements</li>
        <li>You keep ownership of your land during promotion</li>
      </ul>
    </div>
    <div class="split__media reveal"><img src="assets/img/masterplan.svg" alt="Illustration of a masterplan"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">Ways to work together</span><h2>Deals structured around you</h2><p class="lead">Our management structure lets us shape each deal around the individual landowner. Typical routes include:</p></div>
    <div class="grid grid--3" style="margin-top:48px">
      <div class="feature reveal" id="promotion-agreement"><div class="feature__icon">{ICON['map']}</div><h3>Promotion agreement</h3><p>We promote your land at our cost and risk. Once planning is secured, the site is sold on the open market and we receive an agreed share of the proceeds, so our interests are fully aligned with yours.</p></div>
      <div class="feature reveal" id="options"><div class="feature__icon">{ICON['shield']}</div><h3>Option agreement</h3><p>We secure the right to buy your land once planning permission is granted, at an agreed discount to market value. It gives you certainty of a purchaser and a clear route to sale.</p></div>
      <div class="feature reveal" id="sales"><div class="feature__icon">{ICON['pound']}</div><h3>Land with planning</h3><p>We buy land that is ready to develop, including sites with outline planning permission already in place, and give you a quick decision on whether it suits us.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">The journey</span><h2>How the process works</h2></div>
    <div class="process">
      <div class="step reveal"><div class="step__num"></div><h3>Initial appraisal</h3><p>We review planning policy, constraints and market demand, then give you our honest view.</p></div>
      <div class="step reveal"><div class="step__num"></div><h3>Heads of terms</h3><p>We agree the key terms, and your advisers review them with our contribution to their fees.</p></div>
      <div class="step reveal"><div class="step__num"></div><h3>Local Plan</h3><p>We make representations to secure an allocation and build a robust evidence base.</p></div>
      <div class="step reveal"><div class="step__num"></div><h3>Application</h3><p>We consult the community, design a scheme and submit a planning application.</p></div>
      <div class="step reveal"><div class="step__num"></div><h3>Sale &amp; delivery</h3><p>With consent secured, we market the site to achieve best value and see it delivered.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">What we look for</span><h2>Is my land suitable?</h2><p class="lead">We're always seeking new sites and opportunities across our regions, and we welcome approaches from landowners and agents.</p></div>
    <div class="grid grid--4" style="margin-top:48px">
      <div class="feature reveal"><h3>Our regions</h3><p>The North West, North East, Cumbria and Scotland.</p></div>
      <div class="feature reveal"><h3>Edge of settlement</h3><p>Land adjoining existing towns and villages, close to services and transport.</p></div>
      <div class="feature reveal"><h3>With or without planning</h3><p>Land that is ready to develop, and strategic land that doesn't have planning permission yet.</p></div>
      <div class="feature reveal"><h3>Short to long term</h3><p>Short, medium and long-term strategic sites, including some that may take up to 15 years.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream" id="faq">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">FAQs</span><h2>Frequently asked questions</h2></div>
    <div class="faq">
      <details><summary>Who pays for the promotion?</summary><p>We do. Story Homes finances all aspects of land promotion so your risk stays low. The details, including any contribution to your professional fees, are set out in each agreement.</p></details>
      <details><summary>How long does the process take?</summary><p>It depends on the site. Land with outline permission can move quickly, while strategic sites promoted through Local Plans can take up to 15 years. We'll be realistic with you from the start.</p></details>
      <details><summary>Do I still own my land during promotion?</summary><p>Yes. You retain ownership and can continue to farm or use the land as normal until it is sold.</p></details>
      <details><summary>How quickly will I get an answer?</summary><p>Quickly. We aim to tell you promptly whether your site is one we'd look to purchase, so you're not left waiting.</p></details>
      <details><summary>Why work with a housebuilder rather than a promoter?</summary><p>We understand what makes a scheme deliverable and attractive to buyers, which strengthens the planning case and gives confidence that homes will actually be built.</p></details>
    </div>
  </div>
</section>

{TESTIMONIALS}
{CTA}
</main>
""" + FOOTER
write("landowners.html", land)

# ---------------- PROJECTS ----------------
projects = head("Projects | Story Homes Land", "Case studies of land promoted by Story Homes Land.") + header("projects.html") + page_hero("Projects","Our projects","A selection of recent planning consents, applications and land acquisitions across our regions. Click through to read the full stories on storyhomes.co.uk.", "masterplan.svg") + f"""<main>
<section class="section">
  <div class="container">
    <div class="filters" role="group" aria-label="Filter projects by region">
      <button class="filter is-active" data-filter="all">All regions</button>
      <button class="filter" data-filter="north-west">North West</button>
      <button class="filter" data-filter="cumbria">Cumbria</button>
      <button class="filter" data-filter="north-east">North East</button>
      <button class="filter" data-filter="scotland">Scotland</button>
    </div>
    <div class="grid grid--3">
{chr(10).join(project_card(p) for p in PROJECTS)}
    </div>
  </div>
</section>
{TESTIMONIALS}
{CTA}
</main>
""" + FOOTER
write("projects.html", projects)

# ---------------- NEWS ----------------
news = head("News | Story Homes Land", "Latest news and insights from Story Homes Land.") + header("news.html") + page_hero("News","News &amp; insights","Planning successes, company news and expert insight on the land and planning market.", "village.svg") + f"""<main>
<section class="section">
  <div class="container">
    <div class="grid grid--3">
{chr(10).join(news_card(n) for n in NEWS)}
    </div>
  </div>
</section>
{CTA}
</main>
""" + FOOTER
write("news.html", news)

# ---------------- CONTACT ----------------
contact = head("Contact Us | Story Homes Land", "Contact Story Homes Land for a free land appraisal.") + header("contact.html") + page_hero("Contact","Talk to our Strategic Land team","We welcome approaches from landowners and agents, and we'll respond quickly.", "meeting.svg") + f"""<main>
<section class="section">
  <div class="container contact-grid">
    <div>
      <h2>Submit your land</h2>
      <p class="lead" style="margin-bottom:32px">Tell us about your site and a member of the Strategic Land team will respond quickly.</p>
      <form class="form" novalidate>
        <div><label for="name">Full name *</label><input id="name" name="name" required autocomplete="name"></div>
        <div><label for="email">Email *</label><input id="email" name="email" type="email" required autocomplete="email"></div>
        <div><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
        <div><label for="type">I am a…</label><select id="type" name="type"><option>Landowner</option><option>Agent / adviser</option><option>Developer</option><option>Other</option></select></div>
        <div class="form__full"><label for="location">Site location / postcode *</label><input id="location" name="location" required></div>
        <div><label for="size">Approximate size (acres)</label><input id="size" name="size" inputmode="decimal"></div>
        <div><label for="use">Current use</label><select id="use" name="use"><option>Agricultural</option><option>Paddock / grazing</option><option>Brownfield</option><option>Other</option></select></div>
        <div class="form__full"><label for="message">Tell us about your land</label><textarea id="message" name="message"></textarea></div>
        <div class="form__full form__check"><input id="consent" type="checkbox" required><label for="consent" style="font-weight:400;color:inherit">I agree to Story Homes Land contacting me about my enquiry in line with the privacy policy. *</label></div>
        <div class="form__full"><button class="btn btn--dark arrow" type="submit">Send enquiry</button></div>
      </form>
      <div class="form__success" role="status">Thank you. Your enquiry has been received and a member of our land team will be in touch shortly.</div>
    </div>
    <aside>
{chr(10).join(f'      <div class="office"><h3>{n}</h3><p>{r}</p><p style="margin-top:10px"><a href="tel:{t.replace(" ","")}">{t}</a><br><a href="mailto:{e}">{e}</a></p></div>' for n,r,t,e in CONTACTS)}
      <div class="office"><h3>Planning applications</h3><p>For current applications and consultations, visit the <a href="{SH}/land-and-planning/planning-applications/" target="_blank" rel="noopener">Story Homes planning applications page</a>.</p></div>
    </aside>
  </div>
</section>
</main>
""" + FOOTER
write("contact.html", contact)
print("ok")
