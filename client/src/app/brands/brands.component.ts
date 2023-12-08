import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { BRANDS } from '../../constants';
import { CommonModule } from '@angular/common';
import { LazyLoadImageModule } from 'ng-lazyload-image';

@Component({
  selector: 'app-brands',
  standalone: true,
  imports: [CommonModule, LazyLoadImageModule],
  templateUrl: './brands.component.html',
  styleUrl: './brands.component.css',
})
export class BrandsComponent {
  brands = BRANDS;

  @ViewChild('brandGrid') brandGrid!: ElementRef;

  constructor() {}

  ngOnInit(): void {}
}
