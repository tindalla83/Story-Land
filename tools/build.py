import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE = "0000 000 0000"
EMAIL = "land@example.com"

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
        <p style="margin-top:20px">The strategic land and promotion arm of Story Homes, working with landowners to unlock the value of their land through the planning system.</p>
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
          <li><a href="landowners.html#promotion">Land Promotion</a></li>
          <li><a href="landowners.html#options">Option Agreements</a></li>
          <li><a href="landowners.html#sales">Outright Purchase</a></li>
          <li><a href="landowners.html#faq">FAQs</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li><a href="tel:{PHONE.replace(' ','')}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Head Office address<br>Town, Postcode</li>
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
        <p>Speak to our land team for a free, confidential and no-obligation appraisal of your site. We'll give you an honest view of its prospects.</p>
      </div>
      <div class="cta-band__actions">
        <a class="btn btn--primary arrow" href="contact.html">Request a land appraisal</a>
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
 ("north-west","North West","Land north of Meadow Lane","village.svg","Outline consent secured for a sustainable village extension with new public open space and a play area.","32","280","Consented"),
 ("cumbria","Cumbria","Fellside Farm","fields.svg","A former agricultural holding allocated in the emerging Local Plan following our representations.","18","150","Allocated"),
 ("north-east","North East","Hillcrest Meadows","masterplan.svg","A landscape-led masterplan delivering family homes, affordable housing and a new community orchard.","45","400","Consented"),
 ("scotland","Scotland","Burnside Park","hero-landscape.svg","Planning permission in principle granted for a phased development on the edge of an established town.","26","220","Consented"),
 ("north-west","North West","Oakfield Road","meeting.svg","Working with three neighbouring landowners under a collaboration agreement to bring forward a comprehensive scheme.","60","550","In promotion"),
 ("cumbria","Cumbria","Beckside Pastures","village.svg","Full planning permission secured and the site is now under construction by Story Homes.","12","95","Under construction"),
]

def project_card(p, delay=""):
    region, rname, name, img, text, acres, homes, status = p
    return f"""      <article class="card reveal" data-region="{region}">
        <div class="card__media"><img src="assets/img/{img}" alt="Illustration of {name}"></div>
        <div class="card__body">
          <div class="card__meta">{rname} · {status}</div>
          <h3>{name}</h3>
          <p>{text}</p>
          <div class="card__facts"><span><strong>{acres}</strong>acres</span><span><strong>{homes}</strong>homes</span></div>
          <a class="card__link" href="projects.html">View project</a>
        </div>
      </article>"""

NEWS = [
 ("fields.svg","Planning","12 September 2026","Outline consent secured for 280 homes","Our planning team secured outline consent following a positive committee resolution, delivering a strong result for the landowning family."),
 ("masterplan.svg","Insight","28 August 2026","What the latest planning reforms mean for landowners","We look at how recent changes to national planning policy could affect the prospects of land on the edge of settlements."),
 ("meeting.svg","Company","3 August 2026","Story Homes Land expands its team","We've welcomed two new land managers to support our growing pipeline across the North of England and Scotland."),
 ("village.svg","Planning","15 July 2026","Site allocated in emerging Local Plan","Following several years of promotion, our site has been identified as a housing allocation in the draft Local Plan."),
 ("hero-landscape.svg","Insight","1 July 2026","Option agreement or promotion agreement?","A plain-English guide to the most common ways landowners can work with a land promoter, and how to choose."),
 ("fields.svg","Community","18 June 2026","Community consultation draws strong turnout","Over 200 residents attended our consultation event to help shape proposals for new homes and green space."),
]

def news_card(n):
    img, cat, date, title, text = n
    return f"""      <article class="card reveal">
        <div class="card__media"><img src="assets/img/{img}" alt=""></div>
        <div class="card__body">
          <div class="card__meta">{cat} · {date}</div>
          <h3>{title}</h3>
          <p>{text}</p>
          <a class="card__link" href="news.html">Read more</a>
        </div>
      </article>"""

TESTIMONIALS = f"""<section class="section section--cream">
  <div class="container">
    <div class="center"><span class="eyebrow">What landowners say</span></div>
    <div class="slider quote">
      <div class="slide"><blockquote>The team were straightforward from day one. They explained every stage of the planning process and kept us informed throughout. We couldn't have asked for more.</blockquote><cite><strong>Landowner</strong> · Placeholder testimonial, North West</cite></div>
      <div class="slide"><blockquote>Having a housebuilder behind the promotion gave us real confidence that the site would actually be delivered once planning was secured.</blockquote><cite><strong>Farming family</strong> · Placeholder testimonial, Cumbria</cite></div>
      <div class="slide"><blockquote>They took the time to understand what mattered to our family and structured an agreement that worked for everyone involved.</blockquote><cite><strong>Estate trustee</strong> · Placeholder testimonial, Scotland</cite></div>
      <div class="slider__dots"></div>
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
      <p>We partner with landowners to secure planning permission and achieve the best possible value for land with development potential, backed by the strength of Story Homes.</p>
      <div class="hero__ctas">
        <a class="btn btn--primary arrow" href="contact.html">Get a free land appraisal</a>
        <a class="btn btn--ghost" href="landowners.html">How it works</a>
      </div>
    </div>
  </div>
  <a class="hero__scroll" href="#intro">Scroll</a>
</section>

<div class="stats" aria-label="Key figures">
  <div class="stat"><div class="stat__num" data-count="5000" data-suffix="+">5,000+</div><div class="stat__label">Acres under promotion</div></div>
  <div class="stat"><div class="stat__num" data-count="12000" data-suffix="+">12,000+</div><div class="stat__label">Plots in our land pipeline</div></div>
  <div class="stat"><div class="stat__num" data-count="95" data-suffix="%">95%</div><div class="stat__label">Planning success rate</div></div>
  <div class="stat"><div class="stat__num" data-count="35" data-suffix="+">35+</div><div class="stat__label">Years of Story Homes</div></div>
</div>

<section class="section" id="intro">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2>A land promoter with a housebuilder behind it</h2>
      <p class="lead">Story Homes Land is the strategic land division of Story Homes, one of the leading independent housebuilders in the North of England and Scotland.</p>
      <p>We work with landowners, farmers, estates and developers to promote land through the planning process. We fund the full cost and risk of the planning process, and our in-house expertise gives landowners certainty that their site will be delivered.</p>
      <ul class="checklist">
        <li>No upfront costs: we fund planning, surveys and technical work</li>
        <li>Your interests aligned with ours to achieve the best value</li>
        <li>A proven housebuilder ready to deliver once consent is secured</li>
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
      <p class="lead">Every piece of land is different. We tailor our approach to your circumstances and goals, and we're open with you at every step.</p>
    </div>
    <div class="grid grid--3" style="margin-top:48px">
      <div class="feature reveal"><div class="feature__icon">{ICON['shield']}</div><h3>We take the risk</h3><p>We cover the costs of promotion, from technical surveys to planning appeals, so you don't have to.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['pound']}</div><h3>Maximising value</h3><p>Our agreements are structured to secure the best possible price for your land on the open market.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['map']}</div><h3>Local knowledge</h3><p>Regional teams who understand local planning policy, politics and the communities we work in.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['people']}</div><h3>In-house expertise</h3><p>Planners, land managers, technical and design specialists working together under one roof.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['home']}</div><h3>Certainty of delivery</h3><p>As part of Story Homes, we have the capability to build out the sites we promote.</p></div>
      <div class="feature reveal"><div class="feature__icon">{ICON['leaf']}</div><h3>Lasting legacy</h3><p>Landscape-led places that respect their setting and create a legacy you can be proud of.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="center reveal">
      <span class="eyebrow">Our process</span>
      <h2>From field to planning permission</h2>
      <p class="lead">A clear, collaborative journey. We manage every stage while keeping you informed and involved.</p>
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
      <div class="reveal"><span class="eyebrow">Our projects</span><h2 style="margin:0">Recent successes</h2></div>
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
TEAM = [("Name Surname","Managing Director"),("Name Surname","Land Director"),("Name Surname","Planning Director"),("Name Surname","Technical Director"),
        ("Name Surname","Senior Land Manager"),("Name Surname","Land Manager"),("Name Surname","Senior Planner"),("Name Surname","Land Coordinator")]
team_html = "\n".join(f"""      <div class="person reveal"><div class="person__photo"><svg viewBox="0 0 200 200"><rect width="200" height="200" fill="#e6f0eb"/><circle cx="100" cy="80" r="36" fill="#9dbd98"/><path d="M30 200c6-44 36-66 70-66s64 22 70 66z" fill="#3d8a6c"/></svg></div><h3>{n}</h3><p>{r}</p></div>""" for n,r in TEAM)

about = head("About Us | Story Homes Land", "Story Homes Land is the strategic land division of Story Homes.") + header("about.html") + page_hero("About Us","About Story Homes Land","The strategic land specialists within Story Homes, combining land promotion expertise with the delivery strength of an established housebuilder.") + f"""<main>
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Our story</span>
      <h2>Rooted in the North, built on relationships</h2>
      <p>Story Homes was founded on a commitment to quality and to the communities it builds in. Story Homes Land extends that commitment to the landowners we partner with.</p>
      <p>We identify land with long-term development potential and promote it through the planning system, managing the process from start to finish. Our teams bring together land, planning, design and technical specialists with deep regional knowledge.</p>
      <p>Because we're part of a housebuilder, we understand what makes a site deliverable, and we can take it all the way from a field to a thriving new neighbourhood.</p>
    </div>
    <div class="split__media reveal"><img src="assets/img/village.svg" alt="Illustration of new homes"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">Our values</span><h2>What guides us</h2></div>
    <div class="grid grid--4" style="margin-top:48px">
      <div class="feature reveal"><h3>Integrity</h3><p>We are honest about a site's prospects and transparent in every agreement we make.</p></div>
      <div class="feature reveal"><h3>Partnership</h3><p>We treat landowners as long-term partners, not transactions.</p></div>
      <div class="feature reveal"><h3>Expertise</h3><p>Specialist knowledge across planning, land, design and infrastructure.</p></div>
      <div class="feature reveal"><h3>Quality</h3><p>We create places people are proud to call home, built to last.</p></div>
    </div>
  </div>
</section>

<div class="stats" aria-label="Key figures">
  <div class="stat"><div class="stat__num" data-count="5000" data-suffix="+">5,000+</div><div class="stat__label">Acres under promotion</div></div>
  <div class="stat"><div class="stat__num" data-count="60" data-suffix="+">60+</div><div class="stat__label">Active sites</div></div>
  <div class="stat"><div class="stat__num" data-count="4">4</div><div class="stat__label">Regional teams</div></div>
  <div class="stat"><div class="stat__num" data-count="35" data-suffix="+">35+</div><div class="stat__label">Years of Story Homes</div></div>
</div>

<section class="section" id="team">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">Our people</span><h2>Meet the team</h2><p class="lead">Experienced land and planning professionals who know the regions we work in.</p></div>
    <div class="grid grid--4" style="margin-top:48px">
{team_html}
    </div>
  </div>
</section>

{CTA}
</main>
""" + FOOTER
write("about.html", about)

# ---------------- LANDOWNERS ----------------
land = head("For Landowners | Story Homes Land", "How Story Homes Land works with landowners to promote land and maximise its value.") + header("landowners.html") + page_hero("For Landowners","Working with landowners","Whether you own a single field or a large estate, we can help you understand your land's potential and take it through the planning system.", "fields.svg") + f"""<main>
<section class="section" id="promotion">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Land promotion</span>
      <h2>What is land promotion?</h2>
      <p>Land promotion is the process of securing planning permission on land that is currently undeveloped, so it can be sold for development at a much higher value than its existing use.</p>
      <p>Obtaining planning permission is complex, expensive and uncertain. A land promoter takes on that cost and risk, bringing the expertise needed to navigate Local Plans, technical studies and planning applications.</p>
      <ul class="checklist">
        <li>We fund all planning, legal and technical costs</li>
        <li>We contribute to your professional fees</li>
        <li>You retain ownership of your land throughout</li>
      </ul>
    </div>
    <div class="split__media reveal"><img src="assets/img/masterplan.svg" alt="Illustration of a masterplan"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">Ways to work together</span><h2>Flexible agreements</h2><p class="lead">We'll recommend the structure that best suits your land, circumstances and objectives.</p></div>
    <div class="grid grid--3" style="margin-top:48px">
      <div class="feature reveal" id="promotion-agreement"><div class="feature__icon">{ICON['map']}</div><h3>Promotion agreement</h3><p>We promote your land at our cost and risk. Once planning is secured, the site is sold on the open market and we receive an agreed share of the proceeds, so our interests are fully aligned with yours.</p></div>
      <div class="feature reveal" id="options"><div class="feature__icon">{ICON['shield']}</div><h3>Option agreement</h3><p>We secure the right to buy your land once planning permission is granted, at an agreed discount to market value. It gives you certainty of a purchaser and a clear route to sale.</p></div>
      <div class="feature reveal" id="sales"><div class="feature__icon">{ICON['pound']}</div><h3>Outright purchase</h3><p>For land with existing planning permission or a strong planning case, we can offer to buy outright, conditionally or unconditionally.</p></div>
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
    <div class="center reveal"><span class="eyebrow">What we look for</span><h2>Is my land suitable?</h2><p class="lead">We're interested in a wide range of sites across the North of England and Scotland. Typically we look for:</p></div>
    <div class="grid grid--4" style="margin-top:48px">
      <div class="feature reveal"><h3>5+ acres</h3><p>Sites of around five acres or more, although we consider smaller sites in the right location.</p></div>
      <div class="feature reveal"><h3>Edge of settlement</h3><p>Land adjoining existing towns and villages, close to services and transport.</p></div>
      <div class="feature reveal"><h3>Any current use</h3><p>Agricultural land, paddocks, brownfield sites and estates of all sizes.</p></div>
      <div class="feature reveal"><h3>Long-term view</h3><p>Promotion can take several years. We're committed for the long haul.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream" id="faq">
  <div class="container">
    <div class="center reveal"><span class="eyebrow">FAQs</span><h2>Frequently asked questions</h2></div>
    <div class="faq">
      <details><summary>How much does it cost me?</summary><p>Nothing. We fund all costs associated with promoting your land through planning, and we typically make a contribution towards your own legal and professional fees.</p></details>
      <details><summary>How long does the process take?</summary><p>It depends on the site and the stage of the Local Plan. It can range from two years to ten years or more. We'll give you a realistic timescale at the outset.</p></details>
      <details><summary>Do I still own my land during promotion?</summary><p>Yes. You retain ownership and can continue to farm or use the land as normal until it is sold.</p></details>
      <details><summary>What happens if planning permission isn't granted?</summary><p>We bear the cost and risk. If we're unsuccessful you won't be out of pocket, and you'll keep any evidence and reports we've produced, as set out in our agreement.</p></details>
      <details><summary>Why choose a promoter backed by a housebuilder?</summary><p>We understand what makes a scheme deliverable and attractive to buyers, which strengthens the planning case and gives confidence that homes will actually be built.</p></details>
    </div>
  </div>
</section>

{TESTIMONIALS}
{CTA}
</main>
""" + FOOTER
write("landowners.html", land)

# ---------------- PROJECTS ----------------
projects = head("Projects | Story Homes Land", "Case studies of land promoted by Story Homes Land.") + header("projects.html") + page_hero("Projects","Our projects","A selection of the sites we've promoted and secured planning on, in partnership with landowners across our regions.", "masterplan.svg") + f"""<main>
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
contact = head("Contact Us | Story Homes Land", "Contact Story Homes Land for a free land appraisal.") + header("contact.html") + page_hero("Contact","Talk to our land team","Tell us about your land and one of our team will be in touch for a confidential, no-obligation conversation.", "meeting.svg") + f"""<main>
<section class="section">
  <div class="container contact-grid">
    <div>
      <h2>Submit your land</h2>
      <p class="lead" style="margin-bottom:32px">The more you can tell us, the quicker we can give you an initial view.</p>
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
      <div class="office"><h3>Head Office</h3><p>Office address line 1<br>Town, County<br>Postcode</p><p style="margin-top:10px"><a href="tel:{PHONE.replace(' ','')}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
      <div class="office"><h3>North West</h3><p>Office address<br>Town, Postcode</p></div>
      <div class="office"><h3>North East</h3><p>Office address<br>Town, Postcode</p></div>
      <div class="office"><h3>Scotland</h3><p>Office address<br>Town, Postcode</p></div>
    </aside>
  </div>
</section>
</main>
""" + FOOTER
write("contact.html", contact)
print("ok")
