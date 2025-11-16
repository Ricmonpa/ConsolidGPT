// ConsolidGPT - JavaScript

// Generar ID de sesión único
const sessionId = 'session_' + Math.random().toString(36).substr(2, 9);

// Stats globales
let stats = {
    consultas: 0,
    reservas: 0,
    comisionTotal: 0
};

// Toggle Sidebar (móvil)
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
}

// Switch entre vistas
function switchView(viewName) {
    // Ocultar todas las vistas
    document.querySelectorAll('.view-container').forEach(view => {
        view.classList.add('hidden');
    });
    
    // Mostrar la vista seleccionada
    const targetView = document.getElementById(viewName + 'View');
    if (targetView) {
        targetView.classList.remove('hidden');
    }
    
    // Actualizar nav items activos
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    const activeNav = document.querySelector(`[data-view="${viewName}"]`);
    if (activeNav) {
        activeNav.classList.add('active');
    }
    
    // Cerrar sidebar en móvil
    if (window.innerWidth <= 768) {
        toggleSidebar();
    }
    
    // Actualizar stats si es dashboard
    if (viewName === 'dashboard') {
        updateDashboardStats();
    }
}

// Actualizar stats del dashboard
function updateDashboardStats() {
    document.getElementById('totalConsultas').textContent = stats.consultas;
    document.getElementById('totalReservas').textContent = stats.reservas;
    document.getElementById('comisionTotal').textContent = `$${stats.comisionTotal.toLocaleString('es-MX', {minimumFractionDigits: 2})}`;
}

// Auto-resize textarea
const messageInput = document.getElementById('messageInput');
messageInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});

// Manejar Enter para enviar
function handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
}

// Enviar mensaje
async function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Incrementar contador de consultas
    stats.consultas++;
    
    // Agregar mensaje del usuario al chat
    addMessage(message, 'user');
    
    // Limpiar input
    input.value = '';
    input.style.height = 'auto';
    
    // Deshabilitar botón de envío
    const sendBtn = document.getElementById('sendBtn');
    sendBtn.disabled = true;
    
    // Mostrar indicador de escritura
    showTypingIndicator();
    
    try {
        // Enviar mensaje al backend
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            })
        });
        
        const data = await response.json();
        
        // Remover indicador de escritura
        removeTypingIndicator();
        
        if (response.ok) {
            // Agregar respuesta del bot
            addMessage(data.response, 'bot');
            
            // Detectar si es una reserva
            if (data.response.includes('RESERVA CONFIRMADA') || data.response.includes('PNR')) {
                stats.reservas++;
                // Extraer precio si está en el mensaje (simplificado)
                const precioMatch = data.response.match(/\$?([\d,]+\.?\d*)\s*MXN/);
                if (precioMatch) {
                    const precio = parseFloat(precioMatch[1].replace(/,/g, ''));
                    stats.comisionTotal += precio * 0.14;
                }
            }
        } else {
            addMessage('❌ Error: ' + (data.error || 'No se pudo procesar tu mensaje'), 'bot');
        }
    } catch (error) {
        removeTypingIndicator();
        addMessage('❌ Error de conexión. Por favor, intenta de nuevo.', 'bot');
        console.error('Error:', error);
    } finally {
        sendBtn.disabled = false;
        input.focus();
    }
}

// Enviar mensaje rápido
function sendQuickMessage(message) {
    document.getElementById('messageInput').value = message;
    sendMessage();
}

// Agregar mensaje al chat
function addMessage(text, sender) {
    const chatContainer = document.getElementById('chatContainer');
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const avatar = document.createElement('div');
    avatar.className = `message-avatar ${sender}-avatar`;
    avatar.textContent = sender === 'user' ? '👤' : ''; // Bot usa imagen de fondo
    
    const content = document.createElement('div');
    content.className = 'message-content';
    
    const messageText = document.createElement('div');
    messageText.className = 'message-text';
    
    // Formatear el texto (convertir saltos de línea y formato básico)
    messageText.innerHTML = formatMessage(text);
    
    content.appendChild(messageText);
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    
    chatContainer.appendChild(messageDiv);
    
    // Detectar y renderizar tarjetas solo para mensajes del bot
    if (sender === 'bot') {
        detectAndRenderCards(text, content);
    }
    
    // Scroll al final
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Formatear mensaje (básico)
function formatMessage(text) {
    // Convertir saltos de línea
    text = text.replace(/\n/g, '<br>');
    
    // Convertir ** en negrita
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Convertir * en bullet points (si está al inicio de línea)
    text = text.replace(/^[\*•]\s/gm, '• ');
    
    return text;
}

// Detectar y renderizar tarjetas en el mensaje
function detectAndRenderCards(text, messageElement) {
    const cardsContainer = document.createElement('div');
    cardsContainer.className = 'cards-container';
    
    let hasCards = false;
    
    // Detectar vuelos
    const flightPattern = /vuelo[s]?.*?(AM\d+|VOLARIS|VIVA\s*AEROBUS|AEROMEXICO)/gi;
    if (flightPattern.test(text)) {
        const flightCard = createFlightCard(text);
        if (flightCard) {
            cardsContainer.appendChild(flightCard);
            hasCards = true;
        }
    }
    
    // Detectar hoteles
    const hotelPattern = /(HYATT\s*ZIVA|HOTEL|RESORT|ALL[\s-]*INCLUSIVE)/gi;
    if (hotelPattern.test(text)) {
        const hotelCard = createHotelCard(text);
        if (hotelCard) {
            cardsContainer.appendChild(hotelCard);
            hasCards = true;
        }
    }
    
    // Detectar paquetes
    const packagePattern = /(PAQUETE|PACKAGE|TODO\s*INCLUIDO.*VUELO)/gi;
    if (packagePattern.test(text)) {
        const packageCard = createPackageCard(text);
        if (packageCard) {
            cardsContainer.appendChild(packageCard);
            hasCards = true;
        }
    }
    
    if (hasCards) {
        messageElement.appendChild(cardsContainer);
    }
}

// Crear tarjeta de vuelo
function createFlightCard(text) {
    // Extraer información del vuelo
    const codeMatch = text.match(/AM\d+|VOLARIS\s*\d+|VIVA\s*\d+/i);
    const timeMatch = text.match(/(\d{1,2}:\d{2}\s*(?:AM|PM))/gi);
    const dateMatch = text.match(/(\d{1,2}\s+(?:Dic|Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic)[a-z]*)/gi);
    const priceMatch = text.match(/\$\s*([\d,]+)/);
    
    const card = document.createElement('div');
    card.className = 'info-card flight-card';
    
    const airline = codeMatch ? (codeMatch[0].includes('AM') ? 'Aeroméxico' : 
                                 codeMatch[0].includes('VOLARIS') ? 'Volaris' : 'Viva Aerobus') : 'Aerolínea';
    const flightCode = codeMatch ? codeMatch[0] : 'AM540';
    const departTime = timeMatch && timeMatch[0] ? timeMatch[0] : '9:00 AM';
    const arriveTime = timeMatch && timeMatch[1] ? timeMatch[1] : '4:30 PM';
    const departDate = dateMatch && dateMatch[0] ? dateMatch[0] : '1 Dic';
    const arriveDate = dateMatch && dateMatch[1] ? dateMatch[1] : '7 Dic';
    const price = priceMatch ? priceMatch[1] : '8,500';
    
    card.innerHTML = `
        <div class="flight-card-header">
            <div class="flight-icon">✈️</div>
            <div class="flight-title">
                <h4>${airline}</h4>
                <div class="flight-code">Vuelo ${flightCode}</div>
            </div>
        </div>
        
        <div class="flight-details">
            <div class="flight-point">
                <div class="flight-time">${departTime}</div>
                <div class="flight-date">${departDate}</div>
                <div class="flight-location">CDMX (MEX)</div>
            </div>
            
            <div class="flight-arrow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
                <div class="flight-duration">~2h 30m</div>
            </div>
            
            <div class="flight-point">
                <div class="flight-time">${arriveTime}</div>
                <div class="flight-date">${arriveDate}</div>
                <div class="flight-location">Cancún (CUN)</div>
            </div>
        </div>
        
        <div class="flight-info-row">
            <span class="flight-info-label">Clase</span>
            <span class="flight-info-value">Turista</span>
        </div>
        
        <div class="flight-info-row">
            <span class="flight-info-label">Equipaje</span>
            <span class="flight-info-value">1 maleta incluida</span>
        </div>
        
        <div class="flight-info-row">
            <span class="flight-info-label">Precio por persona</span>
            <span class="flight-info-value">$${price} MXN</span>
        </div>
        
        <button class="reserve-btn" onclick="handleReservation('vuelo', '${flightCode}')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 11l3 3L22 4"></path>
                <path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"></path>
            </svg>
            Reservar Vuelo
        </button>
    `;
    
    return card;
}

// Crear tarjeta de hotel
function createHotelCard(text) {
    const hotelMatch = text.match(/HYATT\s*ZIVA|HOTEL\s+[\w\s]+/i);
    const priceMatch = text.match(/\$\s*([\d,]+)/);
    const nightsMatch = text.match(/(\d+)\s*noche[s]?/i);
    
    const card = document.createElement('div');
    card.className = 'info-card hotel-card';
    
    const hotelName = hotelMatch ? hotelMatch[0] : 'Hyatt Ziva Cancún';
    const price = priceMatch ? priceMatch[1] : '12,500';
    const nights = nightsMatch ? nightsMatch[1] : '6';
    
    card.innerHTML = `
        <div class="hotel-card-header">
            <div class="hotel-icon">🏨</div>
            <div class="hotel-info">
                <div class="hotel-name">${hotelName}</div>
                <div class="hotel-stars">⭐⭐⭐⭐⭐</div>
                <div class="hotel-location">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle>
                    </svg>
                    Zona Hotelera, Cancún
                </div>
            </div>
        </div>
        
        <div class="hotel-features">
            <div class="hotel-feature">🍽️ All-Inclusive</div>
            <div class="hotel-feature">🏖️ Frente al mar</div>
            <div class="hotel-feature">👶 Kids Club</div>
            <div class="hotel-feature">🏊 Albercas</div>
            <div class="hotel-feature">🍹 Bares</div>
        </div>
        
        <div class="hotel-policies">
            <div class="hotel-policies-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <path d="M12 6v6l4 2"></path>
                </svg>
                Política de Cancelación
            </div>
            <div class="hotel-policies-text">
                Cancelación gratuita hasta 72 horas antes del check-in. 
                Consulta nuestra base de contratos para más detalles.
            </div>
        </div>
        
        <div class="hotel-price">
            <div class="price-info">
                <span class="price-label">Precio total (${nights} noches)</span>
                <span class="price-amount">$${price}</span>
                <span class="price-per">MXN por habitación</span>
            </div>
            <button class="reserve-btn hotel" onclick="handleReservation('hotel', '${hotelName}')">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9 11l3 3L22 4"></path>
                    <path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"></path>
                </svg>
                Reservar
            </button>
        </div>
    `;
    
    return card;
}

// Crear tarjeta de paquete
function createPackageCard(text) {
    const priceMatch = text.match(/\$\s*([\d,]+)/);
    const nightsMatch = text.match(/(\d+)\s*noche[s]?/i);
    
    const card = document.createElement('div');
    card.className = 'info-card package-card';
    
    const price = priceMatch ? priceMatch[1] : '25,000';
    const nights = nightsMatch ? nightsMatch[1] : '6';
    const savings = Math.round(parseInt(price.replace(/,/g, '')) * 0.15).toLocaleString();
    
    card.innerHTML = `
        <div class="package-badge">🎁 PAQUETE ESPECIAL</div>
        <div class="package-title">Paquete Cancún Todo Incluido</div>
        <div class="package-description">
            Disfruta de unas vacaciones inolvidables con todo incluido. 
            Vuelo redondo + Hotel 5 estrellas + Traslados.
        </div>
        
        <div class="package-includes">
            <div class="package-includes-title">✨ Incluye:</div>
            <div class="package-includes-list">
                <div class="package-include-item">Vuelo redondo CDMX-CUN</div>
                <div class="package-include-item">${nights} noches en Hyatt Ziva</div>
                <div class="package-include-item">All-Inclusive Premium</div>
                <div class="package-include-item">Traslados aeropuerto-hotel</div>
                <div class="package-include-item">Acceso a Kids Club</div>
                <div class="package-include-item">Actividades acuáticas</div>
            </div>
        </div>
        
        <div class="package-price-section">
            <div class="package-price-details">
                <span class="package-price-label">Precio por persona</span>
                <span class="package-price-amount">$${price}</span>
                <span class="package-price-savings">💰 Ahorras $${savings} MXN vs compra separada</span>
            </div>
            <button class="reserve-btn package" onclick="handleReservation('paquete', 'Cancún All-Inclusive')">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9 11l3 3L22 4"></path>
                    <path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"></path>
                </svg>
                Reservar Paquete
            </button>
        </div>
    `;
    
    return card;
}

// Manejar reservación
function handleReservation(type, identifier) {
    const messages = {
        'vuelo': `Quiero reservar el vuelo ${identifier}`,
        'hotel': `Quiero reservar el hotel ${identifier}`,
        'paquete': `Quiero reservar el paquete ${identifier}`
    };
    
    // Incrementar contador de reservas
    stats.reservas++;
    
    // Enviar mensaje automático
    const message = messages[type] || `Quiero hacer una reservación de ${type}`;
    document.getElementById('messageInput').value = message;
    sendMessage();
}

// Mostrar indicador de escritura
function showTypingIndicator() {
    const chatContainer = document.getElementById('chatContainer');
    
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.id = 'typingIndicator';
    
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar bot-avatar';
    avatar.textContent = '🤖';
    
    const content = document.createElement('div');
    content.className = 'message-content';
    
    const indicator = document.createElement('div');
    indicator.className = 'message-text';
    indicator.innerHTML = '<div class="typing-indicator"><span></span><span></span><span></span></div>';
    
    content.appendChild(indicator);
    typingDiv.appendChild(avatar);
    typingDiv.appendChild(content);
    
    chatContainer.appendChild(typingDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Remover indicador de escritura
function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) {
        indicator.remove();
    }
}

// Reiniciar chat
async function resetChat() {
    if (!confirm('¿Estás seguro de que quieres reiniciar la conversación?')) {
        return;
    }
    
    try {
        const response = await fetch('/api/reset', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                session_id: sessionId
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            // Limpiar chat
            const chatContainer = document.getElementById('chatContainer');
            chatContainer.innerHTML = '';
            
            // Agregar mensaje de bienvenida
            addMessage(data.greeting, 'bot');
            
            // Agregar botones rápidos
            const lastMessage = chatContainer.lastElementChild;
            const messageText = lastMessage.querySelector('.message-text');
            messageText.innerHTML += `
                <div class="quick-actions">
                    <button class="quick-btn" onclick="sendQuickMessage('Necesito un viaje familiar a Cancún')">
                        ✈️ Viaje a Cancún
                    </button>
                    <button class="quick-btn" onclick="sendQuickMessage('¿Cuáles son las políticas de cancelación?')">
                        📜 Políticas
                    </button>
                    <button class="quick-btn" onclick="sendQuickMessage('¿Qué incluye el kids club?')">
                        👶 Kids Club
                    </button>
                </div>
            `;
        }
    } catch (error) {
        alert('Error al reiniciar el chat');
        console.error('Error:', error);
    }
}

// Inicialización
window.addEventListener('load', () => {
    // Mostrar chat (New Search) por defecto
    switchView('chat');
    
    // Focus en input si está en vista de chat
    const messageInput = document.getElementById('messageInput');
    if (messageInput) {
        messageInput.focus();
    }
    
    // Actualizar stats iniciales
    updateDashboardStats();
});
