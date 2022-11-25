<!DOCTYPE html>
<!--[if IE]><![endif]-->
<html>
    
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
      <title>Class EnsureObjectStates
     | DisCatSharp Docs </title>
      <meta name="viewport" content="width=device-width">
      <meta name="title" content="Class EnsureObjectStates
     | DisCatSharp Docs ">
      <meta name="generator" content="docfx 2.60.1.0">
      
    <link rel="apple-touch-icon" sizes="57x57" href="../../apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="../../apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="../../apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="../../apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="../../apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="../../apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="../../apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="../../apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../../apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192" href="../../android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="../../favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="../../favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="../../favicon-16x16.png">
    <link rel="manifest" href="/manifest.json">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="msapplication-TileImage" content="../../ms-icon-144x144.png">
    <meta name="theme-color" content="#ffffff">
      <link rel="shortcut icon" href="../../favicon.ico">
      <script defer="" src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "de6c22ce0b3e4c17bb78c8c31b4e695b"}'></script>
      <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/night-owl.min.css">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css" integrity="sha384-EvBWSlnoFgZlXJvpzS+MAUEjvN7+gcCwH+qh7GRFOGgZO0PuwOFro7qPOJnLfe7l" crossorigin="anonymous">
      <link rel="stylesheet" href="../../src/styles/config.css">
      <link rel="stylesheet" href="../../src/styles/discord.css">
      <link rel="stylesheet" href="../../src/styles/dcs.css">
      <link rel="stylesheet" href="../../src/styles/main.css">
      <link rel="stylesheet" href="../../src/styles/colors.css">
      <link rel="stylesheet" href="../../src/styles/highlight/github-dark.min.css">
      <meta property="docfx:navrel" content="../../toc.html">
      <meta property="docfx:tocrel" content="toc.html">
      
      <meta property="docfx:rel" content="../../">
      <meta property="docfx:newtab" content="true">
    </head>

    <body>
        <div class="top-navbar">
            <a class="burger-icon" onclick="toggleMenu()">
                <svg name="Hamburger" style="vertical-align: middle;" width="34" height="34" viewbox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" clip-rule="evenodd" d="M20 6H4V9H20V6ZM4 10.999H20V13.999H4V10.999ZM4 15.999H20V18.999H4V15.999Z"></path></svg>
            </a>

            
            <a class="navbar-brand" href="../../index.html">
              <img id="logo" class="svg" src="../../logo.png" alt="DisCatSharp">
            </a>
        </div>

        <div class="body-content">
            <div id="blackout" class="blackout" onclick="toggleMenu()"></div>

            <nav id="sidebar" role="navigation">
                <div class="sidebar">
                    
                    <div>
                      <div class="mobile-hide">
                        
                        <a class="navbar-brand" href="../../index.html">
                          <img id="logo" class="svg" src="../../logo.png" alt="DisCatSharp">
                        </a>
                      </div>

                      <div class="sidesearch">
                        <form id="search" role="search" class="search">
                            <i class="bi bi-search search-icon"></i>
                            <input type="text" id="search-query" placeholder="Search" autocomplete="off">
                        </form>
                      </div>
                    
                      <div id="navbar">
                      </div>
                    </div>
                    <div class="sidebar-item-separator"></div>
                        
                        <div id="sidetoggle">
                          <div id="sidetoc"></div>
                        </div>
                </div>
                <div class="footer">
                  <strong>Made with ♥ by AITSYS</strong>
                  
                </div>
            </nav>

            <main class="main-panel">
                
                <div id="search-results" style="display: none;">
                  <h1 class="search-list">Search Results for <span></span></h1>
                  <div class="sr-items">
                    <p class="lsearch"><i class="bi bi-hourglass-split index-loading"></i></p>
                  </div>
                  <ul id="pagination" data-first="First" data-prev="Previous" data-next="Next" data-last="Last"></ul>
                </div>

                <div role="main" class="hide-when-search">
                        
                        <div class="subnav navbar navbar-default">
                          <div class="container hide-when-search" id="breadcrumb">
                            <ul class="breadcrumb">
                              <li></li>
                            </ul>
                          </div>
                        </div>
						
						<div id="sidetoggle">
						  <div id="sidetoc"></div>
						</div>
						<div class="article row grid-right">

                    <article class="content wrap" id="_content" data-uid="DisCatSharp.Common.EnsureObjectStates">
  
  
  <h1 id="DisCatSharp_Common_EnsureObjectStates" data-uid="DisCatSharp.Common.EnsureObjectStates" class="text-break">Class EnsureObjectStates
  </h1>
  <div class="markdown level0 summary"><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="2" sourceendlinenumber="2">Ensures that certain objects have the target state.</p>
</div>
  <div class="markdown level0 conceptual"></div>
  <div class="inheritance">
    <h5>Inheritance</h5>
    <div class="level0"><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.object">Object</a></div>
    <div class="level1"><span class="xref">EnsureObjectStates</span></div>
  </div>
  <h6><strong>Namespace</strong>: <a class="xref" href="DisCatSharp.Common.html">DisCatSharp.Common</a></h6>
  <h6><strong>Assembly</strong>: DisCatSharp.Common.dll</h6>
  <h5 id="DisCatSharp_Common_EnsureObjectStates_syntax">Syntax</h5>
  <div class="codewrapper">
    <pre><code class="lang-csharp hljs">public static class EnsureObjectStates : object</code></pre>
  </div>
  <h3 id="methods">Methods
  </h3>
  <span class="small pull-right mobile-hide">
    <span class="divider">|</span>
    <a href="https://github.com/Aiko-IT-Systems/DisCatSharp/new/main/apiSpec/new?filename=DisCatSharp_Common_EnsureObjectStates_EmptyOrNull__1_System_Nullable_List___0___.md&amp;value=---%0Auid%3A%20DisCatSharp.Common.EnsureObjectStates.EmptyOrNull%60%601(System.Nullable%7BList%7B%60%600%7D%7D)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A">Improve this Doc</a>
  </span>
  <span class="small pull-right mobile-hide">
    <a href="https://github.com/Aiko-IT-Systems/DisCatSharp/blob/main/DisCatSharp.Common/Utilities/EnsureObjectStates.cs/#L59">View Source</a>
  </span>
  <a id="DisCatSharp_Common_EnsureObjectStates_EmptyOrNull_" data-uid="DisCatSharp.Common.EnsureObjectStates.EmptyOrNull*"></a>
  <h4 id="DisCatSharp_Common_EnsureObjectStates_EmptyOrNull__1_System_Nullable_List___0___" data-uid="DisCatSharp.Common.EnsureObjectStates.EmptyOrNull``1(System.Nullable{List{``0}})">EmptyOrNull&lt;T&gt;(Nullable&lt;List&lt;T&gt;&gt;)</h4>
  <div class="markdown level1 summary"><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="2" sourceendlinenumber="2">Checks whether the list is null or empty.</p>
</div>
  <div class="markdown level1 conceptual"></div>
  <h5 class="decalaration">Declaration</h5>
  <div class="codewrapper">
    <pre><code class="lang-csharp hljs">public static bool EmptyOrNull&lt;T&gt;(this List&lt;T&gt;? list)</code></pre>
  </div>
  <h5 class="parameters">Parameters</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.nullable-1">Nullable</a>&lt;<span class="xref">List</span>&lt;T&gt;&gt;</td>
        <td><span class="parametername">list</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">The list to check on.</p>
</td>
      </tr>
    </tbody>
  </table>
  <h5 class="returns">Returns</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Type</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.boolean">Boolean</a></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">True if satisfied, false otherwise.</p>
</td>
      </tr>
    </tbody>
  </table>
  <h5 class="typeParameters">Type Parameters</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="parametername">T</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">Any value type.</p>
</td>
      </tr>
    </tbody>
  </table>
  <span class="small pull-right mobile-hide">
    <span class="divider">|</span>
    <a href="https://github.com/Aiko-IT-Systems/DisCatSharp/new/main/apiSpec/new?filename=DisCatSharp_Common_EnsureObjectStates_EmptyOrNull__2_System_Nullable_Dictionary___0___1___.md&amp;value=---%0Auid%3A%20DisCatSharp.Common.EnsureObjectStates.EmptyOrNull%60%602(System.Nullable%7BDictionary%7B%60%600%2C%60%601%7D%7D)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A">Improve this Doc</a>
  </span>
  <span class="small pull-right mobile-hide">
    <a href="https://github.com/Aiko-IT-Systems/DisCatSharp/blob/main/DisCatSharp.Common/Utilities/EnsureObjectStates.cs/#L40">View Source</a>
  </span>
  <a id="DisCatSharp_Common_EnsureObjectStates_EmptyOrNull_" data-uid="DisCatSharp.Common.EnsureObjectStates.EmptyOrNull*"></a>
  <h4 id="DisCatSharp_Common_EnsureObjectStates_EmptyOrNull__2_System_Nullable_Dictionary___0___1___" data-uid="DisCatSharp.Common.EnsureObjectStates.EmptyOrNull``2(System.Nullable{Dictionary{``0,``1}})">EmptyOrNull&lt;T1, T2&gt;(Nullable&lt;Dictionary&lt;T1, T2&gt;&gt;)</h4>
  <div class="markdown level1 summary"><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="2" sourceendlinenumber="2">Checks whether the dictionary is null or empty.</p>
</div>
  <div class="markdown level1 conceptual"></div>
  <h5 class="decalaration">Declaration</h5>
  <div class="codewrapper">
    <pre><code class="lang-csharp hljs">public static bool EmptyOrNull&lt;T1, T2&gt;(this Dictionary&lt;T1, T2&gt;? dictionary)</code></pre>
  </div>
  <h5 class="parameters">Parameters</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.nullable-1">Nullable</a>&lt;<span class="xref">Dictionary</span>&lt;T1, T2&gt;&gt;</td>
        <td><span class="parametername">dictionary</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">The dictionary to check on.</p>
</td>
      </tr>
    </tbody>
  </table>
  <h5 class="returns">Returns</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Type</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.boolean">Boolean</a></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">True if satisfied, false otherwise.</p>
</td>
      </tr>
    </tbody>
  </table>
  <h5 class="typeParameters">Type Parameters</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="parametername">T1</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">Any key type.</p>
</td>
      </tr>
      <tr>
        <td><span class="parametername">T2</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">Any value type.</p>
</td>
      </tr>
    </tbody>
  </table>
  <span class="small pull-right mobile-hide">
    <span class="divider">|</span>
    <a href="https://github.com/Aiko-IT-Systems/DisCatSharp/new/main/apiSpec/new?filename=DisCatSharp_Common_EnsureObjectStates_NotEmptyAndNotNull__1_System_Nullable_List___0___.md&amp;value=---%0Auid%3A%20DisCatSharp.Common.EnsureObjectStates.NotEmptyAndNotNull%60%601(System.Nullable%7BList%7B%60%600%7D%7D)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A">Improve this Doc</a>
  </span>
  <span class="small pull-right mobile-hide">
    <a href="https://github.com/Aiko-IT-Systems/DisCatSharp/blob/main/DisCatSharp.Common/Utilities/EnsureObjectStates.cs/#L68">View Source</a>
  </span>
  <a id="DisCatSharp_Common_EnsureObjectStates_NotEmptyAndNotNull_" data-uid="DisCatSharp.Common.EnsureObjectStates.NotEmptyAndNotNull*"></a>
  <h4 id="DisCatSharp_Common_EnsureObjectStates_NotEmptyAndNotNull__1_System_Nullable_List___0___" data-uid="DisCatSharp.Common.EnsureObjectStates.NotEmptyAndNotNull``1(System.Nullable{List{``0}})">NotEmptyAndNotNull&lt;T&gt;(Nullable&lt;List&lt;T&gt;&gt;)</h4>
  <div class="markdown level1 summary"><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="2" sourceendlinenumber="2">Checks whether the list is not null and not empty.</p>
</div>
  <div class="markdown level1 conceptual"></div>
  <h5 class="decalaration">Declaration</h5>
  <div class="codewrapper">
    <pre><code class="lang-csharp hljs">public static bool NotEmptyAndNotNull&lt;T&gt;(this List&lt;T&gt;? list)</code></pre>
  </div>
  <h5 class="parameters">Parameters</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.nullable-1">Nullable</a>&lt;<span class="xref">List</span>&lt;T&gt;&gt;</td>
        <td><span class="parametername">list</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">The list to check on.</p>
</td>
      </tr>
    </tbody>
  </table>
  <h5 class="returns">Returns</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Type</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.boolean">Boolean</a></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">True if satisfied, false otherwise.</p>
</td>
      </tr>
    </tbody>
  </table>
  <h5 class="typeParameters">Type Parameters</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="parametername">T</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">Any value type.</p>
</td>
      </tr>
    </tbody>
  </table>
  <span class="small pull-right mobile-hide">
    <span class="divider">|</span>
    <a href="https://github.com/Aiko-IT-Systems/DisCatSharp/new/main/apiSpec/new?filename=DisCatSharp_Common_EnsureObjectStates_NotEmptyAndNotNull__2_System_Nullable_Dictionary___0___1___.md&amp;value=---%0Auid%3A%20DisCatSharp.Common.EnsureObjectStates.NotEmptyAndNotNull%60%602(System.Nullable%7BDictionary%7B%60%600%2C%60%601%7D%7D)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A">Improve this Doc</a>
  </span>
  <span class="small pull-right mobile-hide">
    <a href="https://github.com/Aiko-IT-Systems/DisCatSharp/blob/main/DisCatSharp.Common/Utilities/EnsureObjectStates.cs/#L50">View Source</a>
  </span>
  <a id="DisCatSharp_Common_EnsureObjectStates_NotEmptyAndNotNull_" data-uid="DisCatSharp.Common.EnsureObjectStates.NotEmptyAndNotNull*"></a>
  <h4 id="DisCatSharp_Common_EnsureObjectStates_NotEmptyAndNotNull__2_System_Nullable_Dictionary___0___1___" data-uid="DisCatSharp.Common.EnsureObjectStates.NotEmptyAndNotNull``2(System.Nullable{Dictionary{``0,``1}})">NotEmptyAndNotNull&lt;T1, T2&gt;(Nullable&lt;Dictionary&lt;T1, T2&gt;&gt;)</h4>
  <div class="markdown level1 summary"><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="2" sourceendlinenumber="2">Checks whether the dictionary is not null and not empty.</p>
</div>
  <div class="markdown level1 conceptual"></div>
  <h5 class="decalaration">Declaration</h5>
  <div class="codewrapper">
    <pre><code class="lang-csharp hljs">public static bool NotEmptyAndNotNull&lt;T1, T2&gt;(this Dictionary&lt;T1, T2&gt;? dictionary)</code></pre>
  </div>
  <h5 class="parameters">Parameters</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.nullable-1">Nullable</a>&lt;<span class="xref">Dictionary</span>&lt;T1, T2&gt;&gt;</td>
        <td><span class="parametername">dictionary</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">The dictionary to check on.</p>
</td>
      </tr>
    </tbody>
  </table>
  <h5 class="returns">Returns</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Type</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a class="xref" href="https://learn.microsoft.com/dotnet/api/system.boolean">Boolean</a></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">True if satisfied, false otherwise.</p>
</td>
      </tr>
    </tbody>
  </table>
  <h5 class="typeParameters">Type Parameters</h5>
  <table class="table table-bordered table-striped table-condensed">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="parametername">T1</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">Any key type.</p>
</td>
      </tr>
      <tr>
        <td><span class="parametername">T2</span></td>
        <td><p sourcefile="api/DisCatSharp.Common/DisCatSharp.Common.EnsureObjectStates.yml" sourcestartlinenumber="1" sourceendlinenumber="1">Any value type.</p>
</td>
      </tr>
    </tbody>
  </table>

</article>
                </div>

                <div class="copyright-footer">
                    <span>&#169; Aiko IT Systems. All rights reserved.</span>
                </div>
            </div></main>
        

        
        <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
        <script type="text/javascript" src="../../src/scripts/docfx.vendor.js"></script>
        <script type="text/javascript" src="../../src/scripts/docfx.js"></script>
        <script type="text/javascript" src="../../src/scripts/url.min.js"></script>
        <script type="text/javascript" src="../../src/scripts/highlight/highlight.min.js"></script>
        <script>hljs.highlightAll();</script>
        <script src="https://cdn.jsdelivr.net/npm/anchor-js/anchor.min.js"></script>
        <script type="text/javascript" src="../../src/scripts/jquery.twbsPagination.js"></script>
        <script type="text/javascript" src="../../src/scripts/dcs.js"></script>
        <script type="text/javascript" src="../../src/scripts/lunr.js"></script>
    </div></body>
</html>