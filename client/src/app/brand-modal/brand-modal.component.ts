import { Component, Input, Output, EventEmitter } from '@angular/core';
import Brand from '../brands/Brand';

@Component({
  selector: 'app-brand-modal',
  standalone: true,
  imports: [],
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
