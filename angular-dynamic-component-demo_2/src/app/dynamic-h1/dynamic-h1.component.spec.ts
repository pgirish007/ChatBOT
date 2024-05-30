import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DynamicH1Component } from './dynamic-h1.component';

describe('DynamicH1Component', () => {
  let component: DynamicH1Component;
  let fixture: ComponentFixture<DynamicH1Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DynamicH1Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DynamicH1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
