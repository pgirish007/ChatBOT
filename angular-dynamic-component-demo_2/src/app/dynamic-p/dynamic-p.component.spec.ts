import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DynamicPComponent } from './dynamic-p.component';

describe('DynamicPComponent', () => {
  let component: DynamicPComponent;
  let fixture: ComponentFixture<DynamicPComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DynamicPComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DynamicPComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
