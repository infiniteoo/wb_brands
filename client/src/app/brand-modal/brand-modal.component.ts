import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import Brand from '../brands/Brand';

@Component({
  selector: 'app-brand-modal',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './brand-modal.component.html',
  styleUrl: './brand-modal.component.css',
})
export class BrandModalComponent {
  @Input() selectedBrand: Brand | null;
  @Output() closeModalEvent = new EventEmitter<void>();
  constructor() {
    this.selectedBrand = null;
  }

  ngOnInit(): void {}
  closeModal(): void {
    this.closeModalEvent.emit();
  }
}
