import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { BrandsComponent } from './brands/brands.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { HeroComponent } from './hero/hero.component';
import { HeaderComponent } from './header/header.component';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';

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
    HttpClientModule,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'client';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get('http://localhost:8000/api/brands').subscribe((response) => {
      console.log(response);
    });
  }

  performSearch(query: string) {
    // Implement your search logic here using the 'query' parameter.
    console.log('Performing search with query:', query);
    // Example: Call an API or filter data accordingly.
    this.http
      .get('http://localhost:8000/api/brand-search')
      //.get('http://localhost:8000/api/search-brands?query=' + query)
      .subscribe((response) => {
        console.log(response);
      });
  }
}
