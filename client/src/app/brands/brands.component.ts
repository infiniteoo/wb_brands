import { Component, ElementRef, ViewChild, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LazyLoadImageModule } from 'ng-lazyload-image';
import { SpinnerComponent } from '../spinner/app-spinner.component';
import Brand from './Brand';
import { BrandModalComponent } from '../brand-modal/brand-modal.component';

@Component({
  selector: 'app-brands',
  standalone: true,
  imports: [
    CommonModule,
    LazyLoadImageModule,
    SpinnerComponent,
    BrandModalComponent,
  ],
  templateUrl: './brands.component.html',
  styleUrl: './brands.component.css',
})
export class BrandsComponent {
  @Input() brands: any = [];
  selectedBrand: Brand | null = null;

  @ViewChild('brandGrid') brandGrid!: ElementRef;

  constructor() {}

  ngOnInit(): void {}

  handleClickImage(brand: Brand, event: MouseEvent): void {
    event.preventDefault();
    this.selectedBrand = brand;
  }

  handleCloseModal(): void {
    this.selectedBrand = null;
  }
}
