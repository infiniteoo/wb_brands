import { Component } from '@angular/core';
import { BRANDS } from '../../constants';

@Component({
  selector: 'app-brands',
  standalone: true,
  imports: [],
  templateUrl: './brands.component.html',
  styleUrl: './brands.component.css',
})
export class BrandsComponent {
  brands = BRANDS;
}
