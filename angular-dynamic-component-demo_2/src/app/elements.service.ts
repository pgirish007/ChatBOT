import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Element {
  type: string;
  content: string;
}

@Injectable({
  providedIn: 'root'
})
export class ElementsService {
  private dataUrl = 'assets/elements.json';

  constructor(private http: HttpClient) { }

  getElements(): Observable<Element[]> {
    return this.http.get<Element[]>(this.dataUrl);
  }
}
