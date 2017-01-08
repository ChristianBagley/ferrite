console.log("Loaded " + document.URL);

if(false){
    console.log("Ferrite: skipping this page");
} else {
    html = document.getElementsByTagName("html")[0].outerHTML;
    browser.runtime.sendMessage({
        "html": html,
        "url": window.location.href,
        "timestamp": new Date(),
    });
}

