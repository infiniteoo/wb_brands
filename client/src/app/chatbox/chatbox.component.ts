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
    this.http
      .post('http://localhost:8000/api/chatbot', JSON.stringify(message), {
        headers: headers,
      })
      .subscribe((data) => {
        console.log(data);
      });

    // Add user message to chat
    this.chatMessages.push({ text: this.userMessage, isUser: true });
    this.userMessage = '';

    // Simulate chatbot processing (you can replace this with actual API calls)
    this.isLoading = true;
    setTimeout(() => {
      this.isLoading = false;
      // Add chatbot response to chat (replace with actual chatbot response)
      this.chatMessages.push({ text: 'Chatbot response...', isUser: false });
    }, 2000); // Simulated delay
  }
}
