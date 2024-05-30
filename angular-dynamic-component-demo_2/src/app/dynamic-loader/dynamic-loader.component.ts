import { Component, Input, OnInit, ViewChild, ComponentFactoryResolver, ComponentRef, OnDestroy } from '@angular/core';
import { DynamicHostDirective } from '../dynamic-host.directive';
import { DynamicH1Component } from '../dynamic-h1/dynamic-h1.component';
import { DynamicPComponent } from '../dynamic-p/dynamic-p.component';
import { DynamicButtonComponent } from '../dynamic-button/dynamic-button.component';

@Component({
  selector: 'app-dynamic-loader',
  template: '<ng-template appDynamicHost></ng-template>',
})
export class DynamicLoaderComponent implements OnInit, OnDestroy {
  @Input() element: any;
  @ViewChild(DynamicHostDirective, { static: true }) dynamicHost!: DynamicHostDirective;
  private componentRef!: ComponentRef<any>;

  private componentMapper: { [key: string]: any } = {
    h1: DynamicH1Component,
    p: DynamicPComponent,
    button: DynamicButtonComponent,
  };

  constructor(private componentFactoryResolver: ComponentFactoryResolver) {}

  ngOnInit(): void {
    this.loadComponent();
  }

  ngOnDestroy(): void {
    if (this.componentRef) {
      this.componentRef.destroy();
    }
  }

  private loadComponent(): void {
    const componentType = this.componentMapper[this.element.type];
    const componentFactory = this.componentFactoryResolver.resolveComponentFactory(componentType);

    const viewContainerRef = this.dynamicHost.viewContainerRef;
    viewContainerRef.clear();

    this.componentRef = viewContainerRef.createComponent(componentFactory);
    this.componentRef.instance.content = this.element.content;
  }
}
