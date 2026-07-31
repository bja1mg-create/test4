# Erstellt eine HTML Seite mit Popup
html = """
<html>
<body style="background:black; color:white; font-family:Arial; text-align:center; padding-top:100px">
  <h1>👋 Hallo Christian!</h1>
  <button onclick="alert('🎉 DEIN POPUP! Es funktioniert! 🚀')" 
          style="font-size:30px; padding:20px; background:yellow; cursor:pointer">
    Klick mich!
  </button>
  <p>Dein erstes Popup!</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Webseite erstellt: index.html")
