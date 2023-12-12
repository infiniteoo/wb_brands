import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-chatbox',
  templateUrl: './chatbox.component.html',
  styleUrls: ['./chatbox.component.css'],
  standalone: true,
  imports: [FormsModule, CommonModule],
})
export class ChatboxComponent {
  chatMessages: { text: string; isUser: boolean }[] = [];
  userMessage: string = '';
  isLoading: boolean = false;

  // Function to send a message
  sendMessage() {
    if (this.userMessage.trim() === '') return;

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
