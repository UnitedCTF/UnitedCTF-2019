/*@flow*/

import { Panel } from './panel.js';

export class BugReport {
  panel: Panel;

  constructor() {
    this.panel = new Panel('/report-form', '.open-bug-report', '.close-bug-report');
  }
}
