import { test, expect } from '@playwright/test';

// Classe Válida 
test('test', async ({ page }) => {
  await page.goto('https://practicetestautomation.com/practice-test-login/');
  await page.locator('#main-container').click();
  await page.getByRole('textbox', { name: 'Username' }).fill('student');
  await page.getByRole('textbox', { name: 'Username' }).press('Enter');
  await page.getByRole('textbox', { name: 'Password' }).click();
  await page.getByRole('textbox', { name: 'Password' }).fill('Password123');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.locator('h1.post-title')).toHaveText('Logged In Successfully');
});

// Classe Inválida 
test('Teste de Login com Usuário Inexistente', async ({ page }) => {
  await page.goto('https://practicetestautomation.com/practice-test-login/');
  await page.getByRole('textbox', { name: 'Username' }).fill('usuario_errado');
  await page.getByRole('textbox', { name: 'Password' }).fill('Password123');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.locator('#error')).toHaveText('Your username is invalid!');
});

test('Teste de Login com Senha Incorreta', async ({ page }) => {
  await page.goto('https://practicetestautomation.com/practice-test-login/');
  await page.getByRole('textbox', { name: 'Username' }).fill('student');
  await page.getByRole('textbox', { name: 'Password' }).fill('senha_errada');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.locator('#error')).toHaveText('Your password is invalid!');
});

// Valor Limite
test('Teste de Login com Usuário de 1 Caractere', async ({ page }) => {
  await page.goto('https://practicetestautomation.com/practice-test-login/');
  await page.getByRole('textbox', { name: 'Username' }).fill('a');
  await page.getByRole('textbox', { name: 'Password' }).fill('Password123');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.locator('#error')).toHaveText('Your username is invalid!');
});

test('Teste de Login com Usuário Vazio', async ({ page }) => {
  await page.goto('https://practicetestautomation.com/practice-test-login/');
  await page.getByRole('textbox', { name: 'Username' }).fill('');
  await page.getByRole('textbox', { name: 'Password' }).fill('Password123');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.locator('#error')).toHaveText('Your username is invalid!');
});

test('Teste de Login com Senha Vazia', async ({ page }) => {
  await page.goto('https://practicetestautomation.com/practice-test-login/');
  
  await page.getByRole('textbox', { name: 'Username' }).fill('student');
  await page.getByRole('textbox', { name: 'Password' }).fill('');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.locator('#error')).toHaveText('Your password is invalid!');
});