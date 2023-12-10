import { Component } from '@angular/core';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { ProgressSpinnerMode } from '@angular/material/progress-spinner';

/**
 * @title Configurable progress spinner
 */
@Component({
  selector: 'app-spinner',
  templateUrl: 'app-spinner.component.html',
  styleUrls: ['app-spinner.component.css'],
  imports: [MatProgressSpinnerModule],
  standalone: true,
})
export class SpinnerComponent {
  color = 'warn';
  mode: ProgressSpinnerMode = 'indeterminate'; // Explicitly declaring the type
  value = 0;

  constructor() {}

  ngOnInit() {}
}
