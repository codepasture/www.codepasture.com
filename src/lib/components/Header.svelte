<script lang="ts">
</script>

<header>
	<nav>
		<a href="/" class="logo">
			<span class="logo-text"><span class="logo-accent">~/</span>code-pasture</span>
		</a>
		<ul class="nav-links">
			<li><a href="#services">services</a></li>
			<li><a href="#projects">projects</a></li>
			<li><a href="#about">about</a></li>
			<li><a href="#contact" class="btn-nav">start_project()</a></li>
		</ul>
	</nav>
</header>

<style>
	header {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		background: rgba(15, 20, 25, 0.95);
		backdrop-filter: blur(10px);
		border-bottom: 1px solid var(--color-border);
		z-index: 100;
	}

	nav {
		max-width: var(--max-width);
		margin: 0 auto;
		padding: 1rem 2rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.logo {
		text-decoration: none;
		color: var(--color-text);
	}

	.logo-text {
		font-family: var(--font-mono);
		font-size: 1rem;
		color: var(--color-text);
	}

	.logo-accent {
		color: var(--color-accent);
	}

	.nav-links {
		display: flex;
		gap: 2rem;
		list-style: none;
	}

	.nav-links a {
		color: var(--color-text-muted);
		text-decoration: none;
		font-family: var(--font-mono);
		font-size: 0.85rem;
		transition: color var(--transition-fast);
	}

	.nav-links a:hover {
		color: var(--color-text);
	}

	.btn-nav {
		background: var(--color-accent);
		color: var(--color-bg) !important;
		padding: 0.5rem 1rem;
		border-radius: var(--radius-md);
		font-weight: 500;
	}

	.btn-nav:hover {
		background: var(--color-accent-hover);
	}

	@media (max-width: 768px) {
		.nav-links {
			display: none;
		}
	}
</style>
