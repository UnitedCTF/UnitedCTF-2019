/* @flow */
import { Panel } from './panel.js';

export class Chat {
  panel: Panel;

  constructor() {
    this.panel = new Panel('/new-chat-box', '.open-chat', '.chat-header-exit');
  }

  async open() {
    await this.panel.open();
    const chatInputBox = document.querySelector('.chat-input-box');
    chatInputBox &&
      chatInputBox instanceof HTMLInputElement &&
      chatInputBox.addEventListener('keypress', (keyboardEvent: KeyboardEvent) => {
        if (keyboardEvent.key == 'Enter') {
          this.sendMessage(chatInputBox.value);
          chatInputBox.value = '';
        }
      });
  }

  close() {
    this.panel.close();
  }

  sendMessage(message: string) {}
}
