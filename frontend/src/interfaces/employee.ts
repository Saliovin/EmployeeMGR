export interface Employee {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  employee_type: string;
  properties: { [key: string]: any };
}
