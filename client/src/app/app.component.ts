import { Component, Output, OnInit, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { BrandsComponent } from './brands/brands.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { HeroComponent } from './hero/hero.component';
import { HeaderComponent } from './header/header.component';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';

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
export class AppComponent implements OnInit {
  title = 'client';

  @Output() brands: any[] = [];
  currentPage = 1;
  totalPages: number = 0;
  private itemsPerPage = 8; // Number of items to load per page
  loading: boolean = false;
  private scrollSubscription: any;
  constructor(private http: HttpClient) {}

  ngOnInit() {
    // Subscribe to the window scroll event
    this.scrollSubscription = this.subscribeToScroll();
  }
  ngOnDestroy() {
    // Unsubscribe from the scroll event when the component is destroyed
    if (this.scrollSubscription) {
      this.scrollSubscription.unsubscribe();
    }
  }

  private subscribeToScroll() {
    return this.http.get('http://localhost:8000/api/brands').subscribe({
      next: (response: any) => {
        console.log('response', response);
        this.brands = [...this.brands, ...response.brands];
        /* console.log('brands', this.brands); */
        this.totalPages = response.total_pages;
        this.currentPage = response.current_page;
        this.loading = false;
      },
      error: (error: any) => {
        console.error('HTTP request error:', error);
        this.loading = false;
      },
    });
  }

  loadBrands(page: number) {
    this.loading = true;
    // Check if the current page is greater than or equal to the total pages
    console.log('page', page);
    console.log('this.currentPage', this.currentPage);
    console.log('this.totalPages', this.totalPages);

    // Set the loading flag to true

    this.http
      .get(
        `http://localhost:8000/api/brands?page=${page}&per_page=${this.itemsPerPage}`
      )
      .subscribe({
        next: (response: any) => {
          console.log('response', response);

          // Update the properties with the response data
          this.brands = [...this.brands, ...response.brands];
          this.totalPages = response.total_pages;
          this.currentPage = response.current_page;

          // Reset the loading flag
          this.loading = false;
        },
        error: (error: any) => {
          console.error('HTTP request error:', error);

          // Reset the loading flag in case of an error
          this.loading = false;
        },
      });
  }

  @HostListener('window:scroll', ['$event'])
  onScroll(event: Event) {
    const windowHeight: number =
      'innerHeight' in window
        ? window.innerHeight
        : document.documentElement.offsetHeight;
    const scrollY: number = window.scrollY;
    const fullHeight: number = document.documentElement.scrollHeight;

    if (scrollY + windowHeight >= fullHeight && !this.loading) {
      console.log('Loading more brands...');
      this.loadBrands(this.currentPage + 1);
    }
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
