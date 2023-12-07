import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LazyLoadImageModule } from 'ng-lazyload-image';
import { BrandsComponent } from './brands/brands.component';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [BrandsComponent],
  imports: [CommonModule, LazyLoadImageModule],
  bootstrap: [AppComponent],
})
export class AppModule {}
