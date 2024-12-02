// const msg: string = "Hello!";
// alert(msg);

interface AppState {
    currentStyle: string;
    styles: { [key: string]: string };
}

const appState: AppState = {
    currentStyle: "page1.css",
    styles: {
        "Purple Style": "css/page1.css",
        "Red Style": "css/page2.css",
        "Dark Style": "css/page3.css",
        "Natural Style": "css/page4.css",
    }
};

function changeStyle(styleName: string): void {
    const link = document.querySelector('link[rel="stylesheet"]') as HTMLLinkElement;
    if (link) {
        link.href = appState.styles[styleName];
        appState.currentStyle = styleName;
    }
}

function generateStyleLinks(): void {
    const container = document.createElement('div');
    container.id = 'style-links';

    for (const style in appState.styles) {
        const link = document.createElement('a');
        link.href = '#';
        link.textContent = `Zmien na  ${style}`;
        link.addEventListener('click', () => changeStyle(style));
        container.appendChild(link);
        container.appendChild(document.createElement('br'));
    }

    document.body.prepend(container);
}

document.addEventListener('DOMContentLoaded', () => {
    generateStyleLinks();
    alert("Dynamic style switcher ready!");
});
