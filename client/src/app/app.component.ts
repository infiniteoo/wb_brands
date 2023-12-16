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
import { SpinnerComponent } from './spinner/app-spinner.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    SpinnerComponent,
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
  @Output() isLoading: boolean = false;
  currentPage = 1;
  totalPages: number = 0;
  private itemsPerPage = 15; // Number of items to load per page
  loading: boolean = false;
  private preLoadThreshold = 0.5; // 20% of the screen height as the pre-loading threshold

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

  // Calculate whether the user has scrolled close to the threshold
  private isNearBottom(
    scrollY: number,
    windowHeight: number,
    documentHeight: number
  ): boolean {
    return (
      scrollY + windowHeight >=
      documentHeight - windowHeight * this.preLoadThreshold
    );
  }

  public subscribeToScroll() {
    return this.http.get('http://localhost:8000/api/brands').subscribe({
      next: (response: any) => {
        this.loading = true;
        this.isLoading = true;
        console.log('response', response);
        this.brands = [...this.brands, ...response.brands];
        /* console.log('brands', this.brands); */
        this.totalPages = response.total_pages;
        this.currentPage = response.current_page;
        this.loading = false;
        this.isLoading = false;
      },
      error: (error: any) => {
        console.error('HTTP request error:', error);
        this.isLoading = false;
        this.loading = false;
      },
    });
  }

  loadBrands(page: number) {
    this.isLoading = true;
    this.loading = true;
    // Check if the current page is greater than or equal to the total pages
    console.log('page', page);
    console.log('this.currentPage', this.currentPage);
    console.log('this.totalPages', this.totalPages);

    // Set the loading flag to true

    this.http
      .get(
        `http://localhost:8000/api/brands?page=${page}&perPage=${this.itemsPerPage}`
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
          this.isLoading = false;
        },
        error: (error: any) => {
          console.error('HTTP request error:', error);

          // Reset the loading flag in case of an error
          this.isLoading = false;
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
    const documentHeight: number = document.documentElement.scrollHeight;

    // Check if the user has scrolled close to the threshold and not currently loading
    if (
      this.isNearBottom(scrollY, windowHeight, documentHeight) &&
      !this.loading
    ) {
      console.log('Loading more brands...');
      this.loadBrands(this.currentPage + 1); // Load more brands
    }
  }

  performSearch(query: string) {
    // Implement your search logic here using the 'query' parameter.
    console.log('Performing search with query:', query);

    // Create an array to store matching brands
    let matchingBrands: any[] = [];

    // Filter the brands array to get the brands that match the query
    for (const brand of this.brands) {
      if (brand.name.toLowerCase().includes(query.toLowerCase())) {
        matchingBrands.push(brand);
      }
    }

    if (matchingBrands.length === 0) {
      console.log('No matching brands found, calling the database query.');

      // If no matching brands found, make a call to the API to search the database
      this.http
        .get('http://localhost:8000/api/brand-search/', {
          params: { query: query },
        })
        .subscribe((response: any) => {
          this.brands = response['results'];
        });
    } else {
      // If matching brands found, assign them to the brands array
      this.brands = matchingBrands;
    }

    if (query.length === 0) {
      console.log('Query is empty, calling subscribe to scroll.');
      this.subscribeToScroll(); // Call the subscribeToScroll function
    }
  }

  handleClearSearch() {
    this.brands = [];
    console.log('calling subscribe to scroll in handleclearsearch');
    this.subscribeToScroll(); // Call the subscribeToScroll function
  }
}
