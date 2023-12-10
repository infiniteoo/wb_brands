import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-slick-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css'],
  standalone: true,
  imports: [FormsModule, CommonModule],
})
export class SearchBarComponent {
  @Input() debounceTime = 300;
  @Input() brands = [];
  @Output() search = new EventEmitter<string>();

  searchQuery = '';

  private searchTimeout: any;

  onSearch() {
    clearTimeout(this.searchTimeout);
    this.searchTimeout = setTimeout(() => {
      this.search.emit(this.searchQuery);
    }, this.debounceTime);
  }

  clearSearch() {
    this.searchQuery = '';
    this.search.emit('');
  }
}
