console.log("Loaded " + document.URL);

if(browser.extension.inIncognitoContext){
    console.log("Ferrite: skipping this page");
} else {
    html = document.getElementsByTagName("html")[0].outerHTML;
    browser.runtime.sendMessage({
        "html": html,
        "url": window.location.href,
        "timestamp": new Date(),
    });
}

