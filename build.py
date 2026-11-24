#!/usr/bin/env python3
"""Build index.html with embedded base64 images."""
import json

with open("images_b64.json", "r") as f:
    b64 = json.load(f)

intro = b64["introduction.jpg"]
hp = b64["Main Point 1 \u2014 AI in Healthcare.jpg"]
ep = b64["Main Point 2 \u2014 AI in Education.jpg"]
tp = b64["Main Point 3 \u2014 AI in Transportation.jpg"]
cp = b64["Conclusion.png"]

slides = []

# Slide 0: Welcome
slides.append('''  <div class="slide divider-slide" data-index="0">
    <div class="divider-ornament"><span></span></div>
    <div class="tag">ENG 111 — Presentation</div>
    <h1 class="big-title">Welcome</h1>
    <p style="font-family:var(--serif); font-style:italic; font-size:20px; color:rgba(243,234,214,0.85);">The Future of AI</p>
    <p style="margin-top:18px; font-size:14px; color:rgba(243,234,214,0.62);">Healthcare &middot; Education &middot; Transportation</p>
  </div>''')

# Slide 1: Title
slides.append(f'''  <div class="slide title-slide" data-index="1">
    <div class="tag">ENG 111 — Presentation</div>
    <h1 style="font-size:42px;">The Future of AI</h1>
    <div class="title-rule"></div>
    <p class="title-sub">Healthcare · Education · Transportation</p>
    <div class="member-grid">
      <div class="member-card"><div class="avatar">01</div><div class="name">Lazim Al Ahasan</div><div class="id">ID 2414159042</div></div>
    </div>
  </div>''')

# Slide 2: Introduction Divider
slides.append('''  <div class="slide divider-slide" data-index="2">
    <div class="divider-ornament"><span></span></div>
    <div class="tag">Introduction</div>
    <h1>What Is Artificial Intelligence?</h1>
    <p>How AI is reshaping the world around us</p>
  </div>''')

# Slide 3: Introduction
slides.append(f'''  <div class="slide" data-index="3">
    <div class="tag">Introduction</div>
    <h1>What Is Artificial Intelligence?</h1>
    <div class="two-col">
      <div>
        <ul>
          <li><strong>AI</strong> means machines that can think, learn, and solve problems like humans.</li>
          <li>It powers things you use daily: search engines, recommendations, voice assistants.</li>
          <li>Today AI moves beyond simple tools — it is becoming a partner in healthcare, education, and transportation.</li>
          <li>This presentation will explore how AI is shaping our future in these three vital fields.</li>
        </ul>
      </div>
      <div>
        <div class="img-wrap"><img src="{intro}" alt="AI Concept"></div>
        <p class="img-cap">Artificial Intelligence shapes our daily world</p>
      </div>
    </div>
    <div class="highlight-box" style="margin-top:18px;">
      <p class="title">Attention Getter</p>
      <p>"Imagine waking up to a doctor who never sleeps, a teacher who knows exactly how you learn, and a car that drives you safely. That is not a movie — it is the direction AI is heading right now."</p>
    </div>
  </div>''')

# Slide 4: Healthcare Divider
slides.append('''  <div class="slide divider-slide" data-index="4">
    <div class="divider-ornament"><span></span></div>
    <div class="tag">Main Point 1</div>
    <h1>AI in Healthcare</h1>
    <p>Saving lives through earlier, smarter diagnosis</p>
  </div>''')

# Slide 5: Healthcare
slides.append(f'''  <div class="slide" data-index="5">
    <div class="tag">Main Point 1</div>
    <h1>AI in Healthcare</h1>
    <div class="two-col">
      <div>
        <ul>
          <li><strong>Early Diagnosis:</strong> AI analyzes X-rays, MRIs, and CT scans to detect cancer and eye disease earlier than traditional methods.</li>
          <li><strong>Drug Discovery:</strong> AI models speed up medicine research, cutting years down to months. Example: DeepMind's AlphaFold predicts protein structures.</li>
          <li><strong>Personalized Treatment:</strong> AI creates custom treatment plans based on each patient's DNA, lifestyle, and medical history.</li>
        </ul>
      </div>
      <div>
        <div class="img-wrap"><img src="{hp}" alt="AI Healthcare"></div>
        <p class="img-cap">AI-powered diagnostics in modern hospitals</p>
      </div>
    </div>
    <div class="highlight-box" style="margin-top:18px;">
      <p class="title">Why It Matters</p>
      <p>AI doesn't replace doctors — it gives them superpowers, catching diseases sooner and treating patients more personally than ever before.</p>
    </div>
  </div>''')

# Slide 6: Education Divider
slides.append('''  <div class="slide divider-slide" data-index="6">
    <div class="divider-ornament"><span></span></div>
    <div class="tag">Main Point 2</div>
    <h1>AI in Education</h1>
    <p>Personalized learning for every student</p>
  </div>''')

# Slide 7: Education
slides.append(f'''  <div class="slide" data-index="7">
    <div class="tag">Main Point 2</div>
    <h1>AI in Education</h1>
    <div class="two-col">
      <div>
        <div class="img-wrap"><img src="{ep}" alt="AI Education"></div>
        <p class="img-cap">Personalized learning powered by AI</p>
      </div>
      <div>
        <ul>
          <li><strong>Personalized Learning:</strong> AI adapts lessons to each student's pace and style — no one left behind or held back.</li>
          <li><strong>Automated Grading:</strong> AI grades quizzes and essays instantly, saving teachers hours every week.</li>
          <li><strong>Smart Tutors:</strong> AI tutoring systems provide 24/7 help, answering questions anytime.</li>
          <li><strong>Accessibility:</strong> Speech-to-text, translation, and reading assistance make learning possible for students with disabilities.</li>
        </ul>
      </div>
    </div>
    <div class="highlight-box" style="margin-top:18px;">
      <p class="title">Key Insight</p>
      <p>The goal is not to replace teachers, but to give them time to focus on what matters most — mentoring, inspiring, and connecting with students.</p>
    </div>
  </div>''')

# Slide 8: Transportation Divider
slides.append('''  <div class="slide divider-slide" data-index="8">
    <div class="divider-ornament"><span></span></div>
    <div class="tag">Main Point 3</div>
    <h1>AI in Transportation</h1>
    <p>Smarter, safer roads ahead</p>
  </div>''')

# Slide 9: Transportation
slides.append(f'''  <div class="slide" data-index="9">
    <div class="tag">Main Point 3</div>
    <h1>AI in Transportation</h1>
    <div class="two-col">
      <div>
        <ul>
          <li><strong>Self-Driving Cars:</strong> Companies like Tesla and Waymo are building vehicles that navigate without human drivers.</li>
          <li><strong>Ride-Sharing & Routing:</strong> AI finds the fastest routes, reduces traffic, and matches passengers efficiently.</li>
          <li><strong>Predictive Maintenance:</strong> AI monitors buses, trains, and planes to predict failures before they happen.</li>
          <li><strong>Safety:</strong> AI in smart traffic systems cuts accidents caused by human error.</li>
        </ul>
      </div>
      <div>
        <div class="img-wrap"><img src="{tp}" alt="AI Transportation"></div>
        <p class="img-cap">Autonomous vehicles navigating city streets</p>
      </div>
    </div>
    <div class="highlight-box" style="margin-top:18px;">
      <p class="title">The Future Outlook</p>
      <p>AUTO (autonomous urban transport) could eliminate traffic congestion, reduce emissions, and make roads safer for pedestrians and cyclists alike.</p>
    </div>
  </div>''')

# Slide 10: Conclusion Divider
slides.append('''  <div class="slide divider-slide" data-index="10">
    <div class="divider-ornament"><span></span></div>
    <div class="tag">Conclusion</div>
    <h1>The Road Ahead</h1>
    <p>Opportunities, challenges, and what comes next</p>
  </div>''')

# Slide 11: Conclusion
slides.append(f'''  <div class="slide" data-index="11">
    <div class="tag">Conclusion</div>
    <h1>The Road Ahead</h1>
    <div class="two-col">
      <div>
        <div class="img-wrap"><img src="{cp}" alt="AI Future"></div>
        <p class="img-cap">The future of AI is bright and full of promise</p>
      </div>
      <div>
        <ul>
          <li>AI is already transforming <strong>healthcare, education, and transportation</strong> — and this is only the beginning.</li>
          <li>Challenges remain: ethics, job displacement, privacy, and fairness must be addressed responsibly.</li>
          <li>The best future is one where AI works <strong>alongside humans</strong>, making life healthier, smarter, and more connected.</li>
          <li>As future engineers and professionals, we have the opportunity to shape AI for the benefit of all.</li>
        </ul>
      </div>
    </div>
    <div class="highlight-box" style="margin-top:18px;">
      <p style="font-size:15.5px; text-align:center; color:var(--ink); font-family:var(--serif); font-style:italic;"><strong>"AI will not replace us — but those who use AI will outpace those who don't."</strong></p>
    </div>
  </div>''')

# Slide 12: Thank You
slides.append('''  <div class="slide divider-slide" data-index="12">
    <div class="divider-ornament"><span></span></div>
    <div class="tag">ENG 111 — Presentation</div>
    <h1 class="big-title">Thank You</h1>
    <p style="font-family:var(--serif); font-style:italic; font-size:20px; color:rgba(243,234,214,0.85);">for your attention</p>
  </div>''')

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Future of AI — ENG 111 Presentation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">
<style>
:root {
  --ink: #1c2536;
  --ink-soft: #3d3f3a;
  --muted: #6b6b60;
  --navy: #12203a;
  --navy-2: #1b2f52;
  --gold: #a97f1f;
  --gold-deep: #8a6a1f;
  --gold-soft: #c9a24a;
  --parchment: #f4ede1;
  --card: #fffdf8;
  --line: #e6dcc8;
  --tint: #faf4e4;
  --serif: "Playfair Display", Georgia, "Times New Roman", serif;
  --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --shadow: 0 24px 60px -22px rgba(23, 35, 54, 0.28), 0 2px 10px rgba(23, 35, 54, 0.06);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-text-size-adjust: 100%; }
body {
  font-family: var(--sans);
  color: var(--ink-soft);
  background: radial-gradient(1200px 500px at 50% -120px, rgba(193, 154, 63, 0.10), transparent 70%), var(--parchment);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 28px 20px 40px;
}
#stage { width: 100%; display: flex; justify-content: center; }
#slide-deck {
  position: relative;
  width: 100%;
  max-width: 900px;
  min-height: 560px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: var(--shadow);
  overflow: hidden;
  transition: transform 0.25s ease-out;
}
.progress-track {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: rgba(201, 162, 74, 0.18);
  z-index: 5;
}
.progress-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--gold-soft), var(--gold));
  transition: width 0.35s ease-out;
}
.slide {
  display: none;
  width: 100%;
  min-height: 560px;
  padding: 42px 48px 58px;
}
.slide.active {
  display: flex;
  flex-direction: column;
  animation: slideInUp 0.45s cubic-bezier(0.22, 1, 0.36, 1) both;
}
.backward .slide.active { animation-name: slideInDown; }
.slide.divider-slide.active { animation-name: dividerIn; }
.slide.leaving { animation: slideOutUp 0.22s ease-in both; pointer-events: none; }
.backward .slide.leaving { animation-name: slideOutDown; }
.slide.divider-slide.leaving { animation-name: dividerOut; }
@keyframes slideInUp { from { opacity: 0; transform: translateY(18px) scale(0.985); filter: blur(3px); } to { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); } }
@keyframes slideInDown { from { opacity: 0; transform: translateY(-18px) scale(0.985); filter: blur(3px); } to { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); } }
@keyframes slideOutUp { from { opacity: 1; transform: translateY(0); filter: blur(0); } to { opacity: 0; transform: translateY(-14px); filter: blur(3px); } }
@keyframes slideOutDown { from { opacity: 1; transform: translateY(0); filter: blur(0); } to { opacity: 0; transform: translateY(14px); filter: blur(3px); } }
@keyframes cardIn { from { opacity: 0; transform: translateY(14px) scale(0.96); } to { opacity: 1; transform: translateY(0) scale(1); } }
@keyframes avatarIn { from { opacity: 0; transform: scale(0.4) rotate(-8deg); } to { opacity: 1; transform: scale(1) rotate(0); } }
@keyframes riseIn { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
@keyframes stageIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes dividerIn { from { opacity: 0; transform: scale(0.97); } to { opacity: 1; transform: scale(1); } }
@keyframes dividerOut { from { opacity: 1; transform: scale(1); } to { opacity: 0; transform: scale(1.03); } }
h1, h2 { font-family: var(--serif); font-weight: 600; color: var(--ink); }
h1 { font-size: 27px; line-height: 1.2; margin: 0 0 8px; }
h2 { font-size: 23px; line-height: 1.25; margin: 0 0 18px; }
h3 { font-size: 14px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: var(--gold-deep); margin: 0 0 12px; }
p, li { font-size: 15px; line-height: 1.68; color: var(--ink-soft); }
ul { padding-left: 22px; margin: 0 0 10px; }
li { margin-bottom: 7px; }
li::marker { color: var(--gold); }
strong { color: var(--ink); font-weight: 600; }
.tag {
  align-self: flex-start;
  display: inline-block;
  padding: 5px 14px;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--gold-deep);
  background: rgba(193, 154, 63, 0.13);
  border: 1px solid rgba(193, 154, 63, 0.28);
  margin-bottom: 16px;
}
.highlight-box {
  background: var(--tint);
  border-radius: 12px;
  border: 1px solid #ead9ae;
  border-left: 3px solid var(--gold);
  padding: 18px 20px;
  margin: 10px 0;
}
.highlight-box p { font-size: 14px; margin: 0; }
.highlight-box .title { font-weight: 700; color: var(--ink); font-size: 14px; letter-spacing: 0.02em; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; align-items: start; }
.img-wrap {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--line);
  margin: 6px 0 8px;
  max-height: 210px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(193,154,63,0.06), transparent 60%), #f3ecdd;
}
.img-wrap img { max-width: 100%; max-height: 205px; width: auto; object-fit: contain; display: block; }
.img-cap { font-size: 12px; text-align: center; color: var(--muted); margin: 0; }
.slide.active .img-wrap { animation: riseIn 0.55s 0.12s cubic-bezier(0.22, 1, 0.36, 1) both; }
.slide.active .highlight-box { animation: riseIn 0.55s 0.18s cubic-bezier(0.22, 1, 0.36, 1) both; }
.divider-slide {
  align-items: center;
  justify-content: center;
  text-align: center;
  background:
    radial-gradient(600px 300px at 50% -60px, rgba(201, 162, 74, 0.16), transparent 70%),
    linear-gradient(135deg, var(--navy), var(--navy-2));
}
.divider-slide .tag { color: #e8c877; background: rgba(232, 200, 119, 0.10); border-color: rgba(232, 200, 119, 0.30); }
.divider-slide h1 { font-size: 42px; color: #f3ead6; margin: 4px 0 16px; }
.divider-slide h1.big-title { font-size: 54px; }
.divider-slide p { font-size: 17px; color: rgba(243, 234, 214, 0.72); }
.divider-ornament { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 18px; }
.divider-ornament::before, .divider-ornament::after { content: ""; width: 56px; height: 1px; background: linear-gradient(90deg, transparent, rgba(232,200,119,0.7)); }
.divider-ornament::after { background: linear-gradient(90deg, rgba(232,200,119,0.7), transparent); }
.divider-ornament span { width: 7px; height: 7px; transform: rotate(45deg); background: #e8c877; }
.title-slide { align-items: center; justify-content: center; text-align: center; }
.title-slide h1 { font-size: 40px; margin: 6px 0 10px; }
.title-rule { width: 72px; height: 3px; background: linear-gradient(90deg, transparent, var(--gold), transparent); margin: 14px auto; border-radius: 2px; }
.title-sub { font-size: 16px; color: var(--muted); margin-bottom: 6px; }
.member-label { margin-top: 26px; }
.member-grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 16px; max-width: 700px; }
.member-card {
  width: 152px;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 16px 10px 14px;
  text-align: center;
  background: #fff;
  transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
  animation: cardIn 0.5s cubic-bezier(0.22, 1, 0.36, 1) backwards;
}
.member-card:hover { transform: translateY(-4px); box-shadow: 0 12px 24px -12px rgba(23, 35, 54, 0.22); border-color: #d9c48e; }
.avatar {
  width: 46px; height: 46px; margin: 0 auto 10px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, var(--navy), var(--navy-2));
  color: #e8c877;
  font-family: var(--serif);
  font-size: 15px;
  font-weight: 700;
  box-shadow: inset 0 0 0 1.5px rgba(232, 200, 119, 0.35);
}
.member-card .name { font-size: 13px; font-weight: 600; color: var(--ink); line-height: 1.3; }
.member-card .id { font-size: 11.5px; color: var(--muted); margin-top: 4px; font-variant-numeric: tabular-nums; }
.nav-bar {
  display: flex; align-items: center; justify-content: space-between; gap: 10px;
  padding: 13px 22px;
  border-top: 1px solid var(--line);
  background: rgba(255, 253, 248, 0.92);
  backdrop-filter: blur(8px);
}
.nav-btn {
  font-family: var(--sans);
  font-size: 13.5px;
  font-weight: 600;
  color: #fff;
  background: var(--ink);
  border: none;
  border-radius: 9px;
  padding: 9px 18px;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.15s;
}
.nav-btn:hover { opacity: 0.88; transform: translateY(-1px); }
.nav-btn:disabled { opacity: 0.3; cursor: not-allowed; transform: none; }
.nav-btn.ghost { background: transparent; color: var(--gold-deep); border: 1.5px solid rgba(169, 127, 31, 0.45); }
.nav-btn.ghost:hover { background: rgba(193, 154, 63, 0.10); }
.counter { font-size: 13px; color: var(--muted); font-variant-numeric: tabular-nums; white-space: nowrap; }
.nav-right { display: flex; align-items: center; gap: 8px; }
#fs-controls { display: none; }
body.presenting { overflow: hidden; padding: 0; background: #07080c; }
body.presenting #stage { position: fixed; inset: 0; z-index: 90; display: flex; align-items: center; justify-content: center; background: radial-gradient(1000px 600px at 50% 0%, rgba(201, 162, 74, 0.05), transparent 60%), #07080c; animation: stageIn 0.3s ease-out both; }
body.presenting #slide-deck { transform-origin: center center; border-radius: 14px; box-shadow: 0 40px 120px -30px rgba(0, 0, 0, 0.8); }
body.presenting .nav-bar { display: none; }
body.presenting #fs-controls { position: fixed; bottom: 18px; left: 50%; transform: translateX(-50%); z-index: 100; display: flex; flex-direction: column; align-items: center; gap: 8px; opacity: 0; transition: opacity 0.3s ease; pointer-events: none; }
body.presenting #fs-controls.visible { opacity: 1; pointer-events: auto; }
.fs-inner { display: flex; align-items: center; gap: 6px; padding: 7px 10px; border-radius: 999px; background: rgba(10, 13, 18, 0.78); border: 1px solid rgba(255, 255, 255, 0.14); backdrop-filter: blur(12px); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45); }
.fs-btn { font-family: var(--sans); font-size: 13px; font-weight: 600; color: #f3ead6; background: transparent; border: none; border-radius: 8px; padding: 7px 12px; cursor: pointer; transition: background 0.2s; }
.fs-btn:hover { background: rgba(255, 255, 255, 0.12); }
.fs-btn.arrow { font-size: 18px; line-height: 1; padding: 7px 10px; }
.fs-counter { font-size: 12.5px; color: rgba(243, 234, 214, 0.85); font-variant-numeric: tabular-nums; padding: 0 6px; }
.fs-exit .kbd { font-size: 10.5px; color: rgba(243, 234, 214, 0.6); border: 1px solid rgba(255, 255, 255, 0.25); border-radius: 5px; padding: 1px 5px; margin-left: 6px; }
.fs-track { width: min(46vw, 460px); height: 2.5px; border-radius: 2px; background: rgba(255, 255, 255, 0.14); overflow: hidden; }
.fs-track .fs-fill { height: 100%; width: 0%; background: linear-gradient(90deg, var(--gold-soft), #e8c877); transition: width 0.35s ease-out; }
:focus-visible { outline: 2px solid var(--gold); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; transition: none !important; } }
@media (max-width: 680px) {
  body { padding: 12px 10px 24px; }
  #slide-deck { border-radius: 14px; }
  .slide { padding: 26px 22px 50px; min-height: 470px; }
  .two-col { grid-template-columns: 1fr; gap: 16px; }
  .title-slide h1 { font-size: 30px; }
  .divider-slide h1 { font-size: 28px; }
  .divider-slide h1.big-title { font-size: 34px; }
  .divider-slide p { font-size: 15px; }
  .member-card { width: 46%; max-width: 148px; }
  .nav-bar { padding: 11px 14px; flex-wrap: wrap; }
  .nav-btn { padding: 8px 12px; font-size: 12.5px; }
  .img-wrap { max-height: 180px; }
  .img-wrap img { max-height: 175px; }
}
</style>
</head>
<body>
<div id="stage">
<div id="slide-deck">
  <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
{slides_str}
  <div class="nav-bar">
    <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">← Previous</button>
    <span class="counter" id="slideCounter" aria-live="polite">1 / 13</span>
    <div class="nav-right">
      <button class="nav-btn ghost" id="fsBtn" onclick="togglePresenting()" aria-label="Start fullscreen slideshow" title="Fullscreen slideshow (F)">⛶ Slideshow</button>
      <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">Next →</button>
    </div>
  </div>
</div>
</div>
<div id="fs-controls" aria-hidden="true">
  <div class="fs-inner">
    <button class="fs-btn arrow" onclick="changeSlide(-1)" aria-label="Previous slide">‹</button>
    <span class="fs-counter" id="fsCounter">1 / 13</span>
    <button class="fs-btn arrow" onclick="changeSlide(1)" aria-label="Next slide">›</button>
    <button class="fs-btn fs-exit" onclick="togglePresenting()" aria-label="Exit slideshow">Exit<span class="kbd">Esc</span></button>
  </div>
  <div class="fs-track"><div class="fs-fill" id="fsProgress"></div></div>
</div>
<script>
(function() {
  var deck = document.getElementById('slide-deck');
  var slides = Array.prototype.slice.call(deck.querySelectorAll('.slide'));
  var total = slides.length;
  var current = 0;
  var body = document.body;
  var counter = document.getElementById('slideCounter');
  var fsCounter = document.getElementById('fsCounter');
  var progress = document.getElementById('progressFill');
  var fsProgress = document.getElementById('fsProgress');
  var prevBtn = document.getElementById('prevBtn');
  var nextBtn = document.getElementById('nextBtn');
  var fsControls = document.getElementById('fs-controls');
  var idleTimer = null;
  function isPresenting() { return body.classList.contains('presenting'); }
  function render() {
    slides.forEach(function(s, i) { s.classList.remove('leaving'); s.classList.toggle('active', i === current); });
    var label = (current + 1) + ' / ' + total;
    if (counter) counter.textContent = label;
    if (fsCounter) fsCounter.textContent = label;
    var pct = ((current + 1) / total * 100).toFixed(2) + '%';
    if (progress) progress.style.width = pct;
    if (fsProgress) fsProgress.style.width = pct;
    if (prevBtn) prevBtn.disabled = current === 0;
    if (nextBtn) nextBtn.disabled = current === total - 1;
    if (isPresenting()) fit();
  }
  var swapTimer = null;
  var target = current;
  function finishSwap() { swapTimer = null; current = target; render(); }
  function go(dir) {
    var n = target + dir;
    if (n < 0 || n >= total) return;
    if (swapTimer) { clearTimeout(swapTimer); swapTimer = null; }
    slides.forEach(function(s) { s.classList.remove('leaving'); });
    slides[current].classList.add('leaving');
    deck.classList.toggle('backward', dir < 0);
    target = n;
    swapTimer = setTimeout(finishSwap, 230);
  }
  function fit() {
    if (!isPresenting()) return;
    var slide = slides[current];
    var w = deck.clientWidth || 900;
    var h = (slide && slide.offsetHeight) || 560;
    var s = Math.min((window.innerWidth - 48) / w, (window.innerHeight - 48) / h);
    s = Math.max(0.3, Math.min(s, 4));
    deck.style.transform = 'scale(' + s + ')';
  }
  function startIdle() {
    if (!isPresenting()) return;
    fsControls.classList.add('visible');
    clearTimeout(idleTimer);
    idleTimer = setTimeout(function() { fsControls.classList.remove('visible'); }, 2600);
  }
  function enterPresenting() {
    body.classList.add('presenting');
    fsControls.setAttribute('aria-hidden', 'false');
    startIdle();
    fit();
    if (document.documentElement.requestFullscreen) { document.documentElement.requestFullscreen().catch(function() {}); }
  }
  function exitPresenting() {
    body.classList.remove('presenting');
    fsControls.setAttribute('aria-hidden', 'true');
    deck.style.transform = '';
    clearTimeout(idleTimer);
    if (document.fullscreenElement && document.exitFullscreen) { document.exitFullscreen().catch(function() {}); }
  }
  function togglePresenting() { if (isPresenting()) { exitPresenting(); } else { enterPresenting(); } }
  document.addEventListener('fullscreenchange', function() { if (!document.fullscreenElement && isPresenting()) exitPresenting(); });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); go(1); }
    else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); go(-1); }
    else if (e.key === ' ' || e.key === 'Spacebar') { e.preventDefault(); go(1); }
    else if (e.key === 'f' || e.key === 'F') { togglePresenting(); }
    else if (e.key === 'Escape' && isPresenting()) { exitPresenting(); }
  });
  document.addEventListener('mousemove', startIdle);
  var resizeRaf = null;
  window.addEventListener('resize', function() { if (!isPresenting()) return; if (resizeRaf) cancelAnimationFrame(resizeRaf); resizeRaf = requestAnimationFrame(fit); });
  window.changeSlide = go;
  window.togglePresenting = togglePresenting;
  render();
})();
</script>
</body>
</html>'''

result = html.replace('{slides_str}', '\n'.join(slides))
with open("index.html", "w", encoding="utf-8") as f:
    f.write(result)
print("Done! index.html created.")
print(f"File size: {len(result):,} bytes")
