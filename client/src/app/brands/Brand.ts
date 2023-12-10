interface Brand {
  id: number;
  name: string;
  image: string;
  description: string;
  createdAt: Date;
  updatedAt: Date;
  CEO: string;
  history: string;
  location: string;
  board_of_directors: Array<string>;
  founder: string;
  founding_year: number;
  number_of_employees: number;
  revenue_information: string;
  popular_brand_content: Array<[]>;
}

export default Brand;
