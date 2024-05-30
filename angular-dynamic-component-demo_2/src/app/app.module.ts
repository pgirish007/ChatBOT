import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

import { AppComponent } from './app.component';
import { ElementsService } from './elements.service';
import { DynamicH1Component } from './dynamic-h1/dynamic-h1.component';
import { DynamicPComponent } from './dynamic-p/dynamic-p.component';
import { DynamicButtonComponent } from './dynamic-button/dynamic-button.component';
import { DynamicLoaderComponent } from './dynamic-loader/dynamic-loader.component';
import { DynamicHostDirective } from './dynamic-host.directive';

@NgModule({
  declarations: [
    AppComponent,
    DynamicH1Component,
    DynamicPComponent,
    DynamicButtonComponent,
    DynamicLoaderComponent,
    DynamicHostDirective,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    CommonModule
  ],
  providers: [ElementsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
