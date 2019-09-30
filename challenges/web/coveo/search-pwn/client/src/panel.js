/* @flow */

export class Panel {
  uri: string;
  wrapper: HTMLElement;
  closeButtonSelector: string;

  constructor(uri: string, openButtonSelector: string, closeButtonSelector: string) {
    this.uri = uri;
    this.wrapper = document.createElement('div');
    this.wrapper.classList.add('panel-wrapper');
    this.closeButtonSelector = closeButtonSelector;
    this.bindOpenButton(openButtonSelector);
  }

  async open() {
    this.close();
    this.bindCloseButton();
    const response = await fetch(this.uri);
    this.wrapper.innerHTML = await response.text();
    document.body && document.body.appendChild(this.wrapper);
  }

  close() {
    this.wrapper && this.wrapper.remove();
  }

  bindOpenButton(buttonSelector: string) {
    const openChatButton = document.querySelector(buttonSelector);
    openChatButton &&
      openChatButton.addEventListener('click', () => {
        this.open();
      });
  }

  bindCloseButton() {
    const chatExitButton = document.querySelector(this.closeButtonSelector);
    chatExitButton &&
      chatExitButton.addEventListener('click', () => {
        this.close();
      });

    document.documentElement &&
      document.documentElement.addEventListener('click', (e: MouseEvent) => {
        if (e.target instanceof HTMLElement && !e.target.closest('.panel-wrapper')) {
          this.close();
        }
      });
  }
}
