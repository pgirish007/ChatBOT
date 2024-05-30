import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-dynamic-h1',
  template: '<h1>{{content}}</h1>',
})
export class DynamicH1Component {
  @Input() content: string = '';
}
