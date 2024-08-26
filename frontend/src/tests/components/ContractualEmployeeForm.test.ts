import ContractualEmployeeForm from '@/components/ContractualEmployeeForm.vue'
import { mount } from '@vue/test-utils'
import { describe, expect, it } from 'vitest'

describe('contractual employee form', () => {
    it('base', () => {
        const form = mount(ContractualEmployeeForm, {
            props: {
                employee: {
                    id: 0,
                    first_name: "test",
                    last_name: "testing",
                    email: "test@test.com",
                    employee_type: "contractual",
                    properties: {},
                  }
            }
        })
        expect(form).toMatchSnapshot()
    })
})