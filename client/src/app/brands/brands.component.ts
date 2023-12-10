import { Component, OnInit, ElementRef, ViewChild, Input } from '@angular/core';
import { BRANDS } from '../../constants';
import { CommonModule } from '@angular/common';
import { LazyLoadImageModule } from 'ng-lazyload-image';
import { SpinnerComponent } from '../spinner/app-spinner.component';

@Component({
  selector: 'app-brands',
  standalone: true,
  imports: [CommonModule, LazyLoadImageModule, SpinnerComponent],
  templateUrl: './brands.component.html',
  styleUrl: './brands.component.css',
})
export class BrandsComponent {
  /* brands = BRANDS; */
  @Input() brands: any = [];

  @ViewChild('brandGrid') brandGrid!: ElementRef;

  constructor() {}

  ngOnInit(): void {
    /* console.log('brands', this.brands); */
  }
}
