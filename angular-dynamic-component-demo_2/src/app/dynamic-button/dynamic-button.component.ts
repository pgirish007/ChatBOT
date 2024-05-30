import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-dynamic-button',
  template: '<button>{{content}}</button>',
})
export class DynamicButtonComponent {
  @Input() content: string = '';
}
