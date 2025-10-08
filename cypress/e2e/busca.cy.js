describe('Testes da Funcionalidade de Busca por País/Região', () => {

  beforeEach(() => {
    cy.visit('https://app.electricitymaps.com/map');
    cy.contains('button', 'Accept', { timeout: 15000 }).click({ force: true });
  });

  // Caso de Teste 01: Busca com nome de país válido e completo
  it('Deve encontrar um país ao buscar pelo nome completo e válido', () => {
    cy.get('input[placeholder="Search areas"]').type('Germany');
    cy.contains('Germany').click();
    
    // VERIFICAÇÃO FINAL: Checa se a URL contém o código da zona correta.
    cy.url().should('include', '/zone/DE');
  });

  // Caso de Teste 02: Busca com nome de país válido parcial
  it('Deve encontrar um país ao buscar por um nome parcial', () => {
    cy.get('input[placeholder="Search areas"]').type('jap');
    cy.contains('Japan').click();
    
    // VERIFICAÇÃO FINAL: Checa se a URL contém o código da zona correta.
    cy.url().should('include', '/zone/JP');
  });

  // Teste da falha de usabilidade que encontramos
  it('Não deve encontrar um país ao buscar com um espaço no final', () => {
    cy.get('input[placeholder="Search areas"]').type('Brasil ');
    cy.contains('Nothing found').should('be.visible');
  });

  // Adicionando os outros casos de teste negativos
  it('Não deve encontrar resultados para um país inexistente', () => {
    cy.get('input[placeholder="Search areas"]').type('Narnia');
    cy.contains('Nothing found').should('be.visible');
  });

  it('Não deve encontrar resultados para caracteres especiais', () => {
    cy.get('input[placeholder="Search areas"]').type('!@#$%');
    cy.contains('Nothing found').should('be.visible');
  });

  it('Não deve encontrar resultados para números', () => {
    cy.get('input[placeholder="Search areas"]').type('12345');
    cy.contains('Nothing found').should('be.visible');
  });

  // Caso de Teste 07: Busca com nome de país válido seguido de um espaço
  it('Deve validar a falha de usabilidade ao buscar com um espaço no final', () => {
    cy.get('input[placeholder="Search areas"]').type('Brasil '); // Digita com espaço
    cy.contains('Nothing found').should('be.visible'); // Verifica o comportamento de falha
  });

});

// Adiciona um "ouvinte" de eventos para exceções não capturadas da aplicação
Cypress.on('uncaught:exception', (err, runnable) => {
  // Verifica se a mensagem de erro inclui QUALQUER UM dos erros conhecidos do React
  if (
    err.message.includes('Minified React error #418') ||
    err.message.includes('Minified React error #423')
  ) {
    // Se for um dos erros conhecidos, retorna false para impedir que o Cypress falhe o teste.
    return false;
  }
// Para qualquer outro erro desconhecido, permite que o Cypress falhe.
  return true;
});
