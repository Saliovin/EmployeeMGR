import RegularEmployeeForm from '@/components/RegularEmployeeForm.vue'
import { mount } from '@vue/test-utils'
import { describe, expect, it } from 'vitest'

describe('regular employee form', () => {
    it('base', () => {
        const form = mount(RegularEmployeeForm, {
            props: {
                employee: {
                    id: 0,
                    first_name: "test",
                    last_name: "testing",
                    email: "test@test.com",
                    employee_type: "regular",
                    properties: {},
                  }
            }
        })
        expect(form.element).toMatchSnapshot()
    })
})