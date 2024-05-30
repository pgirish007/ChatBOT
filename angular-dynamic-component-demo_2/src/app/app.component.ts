import { Component, OnInit } from '@angular/core';
import { ElementsService, Element } from './elements.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  elements: Element[] = [];

  constructor(private elementsService: ElementsService) {}

  ngOnInit(): void {
    this.elementsService.getElements().subscribe(data => {
      this.elements = data;
    });
  }
}
