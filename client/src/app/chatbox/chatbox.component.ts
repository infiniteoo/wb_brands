import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-chatbox',
  templateUrl: './chatbox.component.html',
  styleUrls: ['./chatbox.component.css'],
  standalone: true,
  schemas: [],
  imports: [FormsModule, CommonModule],
})
export class ChatboxComponent {
  chatMessages: { text: string; isUser: boolean }[] = [];
  userMessage: string = '';
  isLoading: boolean = false;

  constructor(private http: HttpClient, private cookieService: CookieService) {}

  // Function to send a message
  sendMessage() {
    this.isLoading = true;
    if (this.userMessage.trim() === '') return;
    // send message to back end
    const csrfToken = this.cookieService.get('troytoken');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken, // Include the CSRF token in the headers
    });
    const message = {
      message: this.userMessage,
    };

    console.log(this.userMessage);
    this.chatMessages.push({ text: this.userMessage, isUser: true });
    this.http
      .post('http://localhost:8000/api/chatbot', JSON.stringify(message), {
        headers: headers,
        responseType: 'json', // Set the response type to JSON
      })
      .subscribe((data: any) => {
        if (data) {
          for (const key in data) {
            if (data.hasOwnProperty(key)) {
              this.chatMessages.push({ text: data[key], isUser: false });
              this.isLoading = false;
              break; // Stop after the first key is found
            }
          }
        }
      });

    // Add user message to chat

    this.userMessage = '';
  }
}
