<div class="card-block">
<div class="row">
<div class="col tab-content">
<div class="tab-pane active show" id="subject" role="tabpanel">
<div class="row">
<div class="col-md-12 col-xl-12">
<div class="markdown-body">
<p class="text-muted m-b-15">
</p><h1>My First Scraper Ds</h1>
<p>Remember to git add &amp;&amp; git commit &amp;&amp; git push each exercise!</p>
<p>We will execute your function with our test(s), please DO NOT PROVIDE ANY TEST(S) in your file</p>
<p>For each exercise, you will have to create a folder and in this folder, you will have additional files that contain your work. Folder names are provided at the beginning of each exercise under <code>submit directory</code> and specific file names for each exercise are also provided at the beginning of each exercise under <code>submit file(s)</code>.</p>
<hr>
<table>
<thead>
<tr>
<th>My First Scraper Ds</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Submit directory</td>
<td>.</td>
</tr>
<tr>
<td>Submit file</td>
<td>my_first_scraper.py</td>
</tr>
</tbody>
</table>
<h3>Description</h3>
<h2>Introduction</h2>
<img src="https://storage.googleapis.com/qwasar-public/track-ds/meme_scraping.png" width="400">
<p>HTML has been built to be "displayed". It's working very well... but when you want to build a script to collect actionable data, you are left with this:</p>
<pre class=" language-plain"><code class=" language-plain">
&lt;!doctype html&gt;&lt;html itemscope="" itemtype="http://schema.org/WebPage" lang="en"&gt;&lt;head&gt;&lt;meta charset="UTF-8"&gt;&lt;meta content="origin" name="referrer"&gt;&lt;meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"&gt;&lt;meta content="noodp" name="robots"&gt;&lt;meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"&gt;&lt;meta content="origin" name="referrer"&gt;&lt;title&gt;Google&lt;/title&gt;&lt;script nonce="RV78oTZM3BoorRaUbY2QZQ=="&gt;(function(){window.google={kEI:'Axs7X5WnBMut0PEPi5OcwAI',kEXPI:'31',u:'8804ad99',kBL:'vHaf'};google.sn='webhp';google.kHL='en';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&amp;&amp;(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&amp;&amp;(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&amp;&amp;google.vel.lu&amp;&amp;google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&amp;ei=")||(e="&amp;ei="+google.getEI(d),-1==c.search("&amp;lei=")&amp;&amp;(d=google.getLEI(d))&amp;&amp;(e+="&amp;lei="+d));d="";!b&amp;&amp;google.cshid&amp;&amp;-
...
window.performance&amp;&amp;window.performance.navigation&amp;&amp;window.performance.navigation.type};function k(a,b){return!a||!b&amp;&amp;l(a)?0:a.getBoundingClientRect?m(a,b,function(c){return c.getBoundingClientRect()}):1}function l(a){if("none"==a.style.display)return!0;if(document.defaultView&amp;&amp;document.defaultView.getComputedStyle){var b=a.getAttribute("data-deferred");b&amp;&amp;a.setAttribute("data-deferred",0);var c=document.defaultView.getComputedStyle(a);c=!!c&amp;&amp;("hidden"==c.visibility||"0px"==c.height&amp;&amp;"0px"==c.width);b&amp;&amp;a.setAttribute("data-deferred",b);return c}return!1}
function m(a,b,c){var d=c(a);a=d.left+window.pageXOffset;c=d.top+window.pageYOffset;var e=d.width;d=d.height;var f=0;if(!b&amp;&amp;0&gt;=d&amp;&amp;0&gt;=e)return f;0&gt;c+d?f=2:c&gt;=(window.innerHeight||document.documentElement.clientHeight)&amp;&amp;(f=4);if(0&gt;a+e||a&gt;=(window.innerWi....
0==c.returnValue)c.returnValue=!0}c=[];for(d=b.a;d;d=d.parentNode)c.push(d);a=a.type;for(d=
c.length-1;0&lt;=d;d--){b.a=c[d];var f=Aa(c[d],a,!0,b);e=e&amp;&amp;f}for(d=0;d&lt;c.length;d++)b.a=c[d],f=Aa(c[d],a,!1,b),e=e&amp;&amp;f}return e}return za(a,new T(b,this))},Y=function(a){a=a[W];return a instanceof V?a:null},Z="__closure_events_fn_"+(1E9*Math.random()&gt;&gt;&gt;0),ua=function(a){if("function"==aa(a))return a;a[Z]||(a[Z]=function(b){return a.handleEvent(b)});return a[Z]};ta(document,"DOMContentLoaded",function(){document.f&amp;&amp;(document.f.q.getAttribute("data-saf")||document.f.q.focus());document.gbqf&amp;&amp;document.gbqf.q.focus();document.images&amp;&amp;((new Image).src=s)});})();&lt;/script&gt;&lt;/div&gt;&lt;textarea class="csi" name="csi" style="display:none"&gt;&lt;/textarea&gt;&lt;script nonce="RV78oTZM3BoorRaUbY2QZQ=="&gt;(function(){
(function(){var c=google.time();if(google.timers&amp;&amp;google.timers.load.t){for(var a=document.getElementsByTagName("img"),d=0,b=void 0;b=a[d++];)google.c.setup(b);google.c.e("load","imn",String(a.length));google.c.ubr(!0,c);google.c.glu&amp;&amp;google.c.glu();google.rll(window,!1,function(){google.tick("load","ol");google.c.u("pr")})}})();}).call(this);google.drty&amp;&amp;google.drty();&lt;/script&gt;&lt;/body&gt;&lt;/html&gt;
</code></pre>
<p><em>Google search page engine HTML</em>
Euuh... I just wanted to collect all the links on the page...</p>
<p>It’s likely that there are libraries to navigate through the jungle. Let's scrap some Data!</p>
<h2>Technical specifications</h2>
<p>Using python libraries <code>requests and beautifulsoup4</code>, return a CSV of the TOP 25 trending repositories from Github.</p>
<ol start="0">
<li>Request (with request)</li>
<li>Extract (with beautifulsoup4)</li>
<li>Transform</li>
<li>Format</li>
</ol>
<img src="https://storage.googleapis.com/qwasar-public/track-ds/github_trending.png" width="700">
<p><a href="https://github.com/trending" target="_blank">Github trending's page</a></p>
<p><strong>Part 0: Request</strong>
Write a function prototyped: <code>def request_github_trending(url)</code> it will return the result of <code>Request</code>.</p>
<p><strong>Part 1: Extract</strong>
Write a function prototyped: <code>def extract(page)</code> to <code>find_all</code> instances of HTML code of repository rows and return it. You should use <code>BeautifulSoup</code>. :-)</p>
<p><strong>Part 2: Transform</strong>
Write a function prototyped: <code>def transform(html_repos)</code> taking an array of all the instances of HTML code of the repository row.
It will return an array of hash following this format: <code>[{'developer': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]</code></p>
<p><strong>Part 3: Format</strong>
Write a function prototyped: <code>def format(repositories_data)</code> taking a repository array of hash and transforming it and returning it into a <code>CSV</code> string. Each column will be separated by <code>,</code> and each line by <code>\n</code>
The columns will be <code>Developer</code>,<code>Repository Name</code>,<code>Number of Stars</code></p>
<p><em>Tip</em>
Google: Request get python
Google: BeautifulSoup python</p>

<p></p>
</div>

</div>
</div>
</div>
<div class="tab-pane" id="resources" role="tabpanel">
</div>
</div>
</div>
</div>
