function rudrSwitchTab(rudr_tab_id, rudr_tab_content) {
    // first of all we get all tab content blocks (I think the best way to get them by class names)
    let tabs = document.getElementsByClassName("tabcontent");
    for (let i = 0; i < tabs.length; i++) {
        tabs[i].style.display = 'none'; // hide all tab content
    }
    document.getElementById(rudr_tab_content).style.display = 'block'; // display the content of the tab we need

    // now we get all tab menu items by class names (use the next code only if you need to highlight current tab)
    let menu = document.getElementsByClassName("tabmenu");
    for (let i = 0; i < menu.length; i++) {
        menu[i].className = 'tabmenu';
    }
    document.getElementById(rudr_tab_id).className = 'tabmenu active';
}