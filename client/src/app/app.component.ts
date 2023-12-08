import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { BrandsComponent } from './brands/brands.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { HeroComponent } from './hero/hero.component';
import { HeaderComponent } from './header/header.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    RouterOutlet,
    BrandsComponent,
    SearchBarComponent,
    HeroComponent,
    HeaderComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'client';

  performSearch(query: string) {
    // Implement your search logic here using the 'query' parameter.
    console.log('Performing search with query:', query);
    // Example: Call an API or filter data accordingly.
  }
}
