import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-dynamic-p',
  template: '<p>{{content}}</p>',
})
export class DynamicPComponent {
  @Input() content: string = '';
}
