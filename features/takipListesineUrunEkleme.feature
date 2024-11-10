Feature: Takip Listesine Ürün Ekleme Özelliği

  @completed
  Scenario: Ürünün başarılı bir şekilde takip listesine eklenmesi
    Given homepage e giriş yapılır
    When kullanıcı bir ürünü aratır
    And kullanıcı gelen ürün listesinden ürün seçimi yapar ve ürüne git seçeneğine tıklar
    Then kullanıcı ürünü takip listesine ekler