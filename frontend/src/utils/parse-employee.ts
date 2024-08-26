export const clean_properties = (
  employee_type: string,
  properties: { [key: string]: any }
) => {
  switch (employee_type) {
    case "contractual":
      return {
        contract_end_date: properties.contract_end_date,
        project: properties.project,
      };
    default:
      return {
        number_of_leaves: properties.number_of_leaves,
        benefits: properties.benefits,
      };
  }
};
